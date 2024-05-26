# django_adx
 
This module enable creating aggregated data on multiple dimensions (CUBE)

It was initially build as part of openimis-be-dhis2_etl_py made by Damian Borowiecki @dborowiecki (models) and Kamil Malinowski @Malinowskikam (dev) and

## concepts

To create a cube that can later be serialized using the ADX format some steps are required

ADX cubes have 3 mandatory dimensions : WHAT (data_value), WHEN and WHERE (org_unit); but more dimension can be added to them, it requires the utilization of category (Very similar of how DHIS2 data element works); here are the step to create 

- creating slices/options including a filter 
- creating Category with their slices

the ADX format use the CODE extensively therefore the WHEN, WHERE, WHAT, CATEGORY and CATEGORY OPTIONS need to have a code
sometime the code need to be resolved that why there is a `to_org_unit_code_func` that can generate the code from the object acting as the org_unit  

## how it works

The adx definition (see example below) include a period type that should be used to create the time filter it also have
a list of groups definition that define the function `period_filter_func`  that will generate the time filter that will be used for all the data_value in that group, this means that a group il likely to host the data_value associated to one django class


 will be added to the "WHAT" django Query after the filter defined to the "WHEN" and "WHERE"


## **ADX Formatting** 

in order to enable combination of the filter using he django ORM 2 concept are important:

- filter: a django Q object that will be applied the the "data element" Query

- link between the "WHERE" and the "WHAT" expressed  `dataset_from_orgunit_func`

## category

example of a method that return a category definition including the slices, this method has a parameter `prefix` so it can be used on object where the gender found  in found through another object e.g `insuree__gender__code`,  then the prefi would be `insuree__`

```python

def get_sex_categories(prefix='') -> ADXMappingCategoryDefinition:
    return ADXMappingCategoryDefinition(
        category_name="sex",
        category_options=[
            ADXCategoryOptionDefinition(
                code="M", name= "MALE", filter= q_with_prefix( 'gender__code', 'M', prefix)),
            ADXCategoryOptionDefinition(
                code="F", name= "FEMALE", filter=q_with_prefix( 'gender__code', 'F', prefix)),
            ADXCategoryOptionDefinition(
                code="O", name= "OTHER", is_default = True)
        ]
    )


```

the `is_default` attribute prevent adding a filter but it also prevent having data that are not covers by any options

The category name is also used for the CODE


### ADX Data definition 
ADX Data definition can be defined using `django_adx.models.adx.ADXMappingDefinition`. 
```python 
ADXMappingDefinition(
    period_type=ISOFormatPeriodType(), # Format of handled period type, at the moment only ISO Format is supported 
    to_org_unit_code_func= lambda l: build_dhis2_id(l.uuid),
    groups=[
        ADXMappingGroupDefinition(
            comment=str, # Generic comment 
            name=str, # Name of ADX Mapping Definition 
            data_values=[
                ADXMappingDataValueDefinition(
                    data_element=str, # Name of calculated value 
                    period_filter_func =  function # function expection an queryset to filter and a period as input and should return a queryset
                    dataset_from_orgunit_func=function # Function extracting collection from group orgunit object
                    aggregation_func=function # Function transforming filtered queryset to dataset value 
                    categories=[
                        ADXMappingCategoryDefinition(
                            category_name=str,
                            category_options=[
                                ADXCategoryOptionDefinition(
                                    code=code,
                                    name=name,
                                    filter=function # Django Q filter to gather the data of that stratifier `dataset_from_orgunit_func`
                                )
    ])])])])
```
#### Example definition: [HF Number of insurees](django_adx/tests/adx_tests.py)

### ADX Data Storage 
`django_adx.converters.adx.ADXBuilder` is used for creating ADX Data collection
based on data definition. 
Example:

```python
from django_adx.converters.adx.builders import ADXBuilder
from django_adx.models.adx.definition import ADXMappingGroupDefinition

definition = ADXMappingGroupDefinition(...)
builder = ADXBuilder(definition)
period_type = "2019-01-01/P2Y"  # In format accepted by definition.period_type
org_units = HealthFaciltity.objects.filter(validity_to__isnull=True)  # All HF
builder.create_adx_cube(period_type, org_units)  # Returns ADXMapping object
```

### ADX Formatters
ADX Formatters allow transforming ADXMapping objects to diffrent formats. 
At the moment only XML Format is implemented.

```python
from django_adx.converters.adx.formatters import XMLFormatter
from django_adx.models.adx.data import ADXMapping

adx_format = ADXMapping(...)
xml_formatter = XMLFormatter()
xml_format = xml_formatter.format_adx(adx_format)
```

## CODE

the code can only be alpha numeric, all other char will be replaced by "_"