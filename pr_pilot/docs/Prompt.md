# Prompt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **str** | The prompt for the task | 
**github_repo** | **str** | The full name of the Github repository, e.g. &#39;owner/repo&#39; | 
**issue_number** | **int** | Number of the issue if task is triggered in the context of an issue | [optional] 
**pr_number** | **int** | Number of the PR if task is triggered in the context of a PR | [optional] 
**branch** | **str** | A branch for PR Pilot to run this task on | [optional] 
**gpt_model** | **str** | The GPT model to use for the task | [optional] [default to 'gpt-4-turbo']
**image** | **str** | An image to be used in the task | [optional] 

## Example

```python
from pr_pilot.models.prompt import Prompt

# TODO update the JSON string below
json = "{}"
# create an instance of Prompt from a JSON string
prompt_instance = Prompt.from_json(json)
# print the JSON string representation of the object
print(Prompt.to_json())

# convert the object into a dict
prompt_dict = prompt_instance.to_dict()
# create an instance of Prompt from a dict
prompt_from_dict = Prompt.from_dict(prompt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


