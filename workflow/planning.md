Working out how to make the model. 
Resources:
- patience
- willpower
- sleep
- finances
- learning
- output
- sociability
- health


What else?
model is made of:
- resources
- actions
- relevent entities
- triggers
- events

The entities have associated actions. 
Actions affect resources. 
Actions are executed when a trigger occurs. 
A list of events hits a series of triggers, executing the actions on the relevant entities to modify the resouces. 


---


Alternative: have code that is a layout of a typical workflow. 
Actions, triggers are built directly into the model. 
Events are series of triggers that are also hardcoded, runs the code in a predictable way. 
Would be too easy to create a model where fuzzing wouldn't show emergent behaviour from stress though, because the model would be tailored to a precise series of events and wouldn't have range/redundant parameters needed when fuzzing occurs. 
- For example, the workflow may never affect finances, but having it there means code fuzzing may expose emergent behaviour when stress is put on the worker and they buy fancier food. 

Best to create a workflow that is a series of responses to events. Then, changes in events can be seperated from changes in model, reflecting *two types of stress on a sociotechnical system that exist*. The code fuzzing should operate on both. 
