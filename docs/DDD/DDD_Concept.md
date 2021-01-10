# Domain Driven Design - Concept
In this post I apply Domain-Driven Design to my Expense Tracker. The resulting code can be found at ----Link-----.

## General Goal
In this project I code an application that gives me insight in my financial situation. The application mainly tells me where you spent your money. As starting point of the application you should set your budget for each category or for all categories together per year/month. After that, the next point is to type in your expenses, but for some reasons, the Expense Tracker is set in a way, where the timestamp of the expenses will calculate the month in which the expenditures where done. So is is important to write down every expense in the month you want them to be. If all this is done, the application can show you a 'View' of your expenses and your budgets with some specifications. 

## Ubiquitous language
For better Domain Driven Design and a good architecture in the code, ubiquitous language should be applied in every Domain. 

The Expense Tracker has 3 different domains, which have some dependencies between them. But every domain has its own 'environment'. 

To get finacial insights it is important to separate budget and expenses. So there are two corresponding domains, which work together, as it gives an overview of your finacial status and your money you have still left in a month. To make this remaining money visible and to give a insight in your expenses, there is a need of a Domain, which corresponds with expenses and budgets together but also with one of these two domains alone. 

The communication and the data exchange between these classes should be regulated with interfaces and other classes. Especially between the Visualization domain and the other domains. 

## Entities and value objects
After defining the ubiquitous language the next step is to define the whole model of the Expense Tracker. One important step is to categorize the entities and the value objects. As defined in the previous chapter there is a need of 3 specific objects: Budget, Expenditure and View. It is clear that View is an entity, because if the budget changes or if there are expenditures which coming in, the View will always be a different one than it was before. The Budget should also be declared as an entity because the budget can change every time, especially when it is calculated every month. The expenditures itself are much more difficult to declare, because if there is a expenditures it couldn't be reversed or changed. It is immutable and therefore it is declared as a value object. We leave the fact, that for instance, if you give back bought shoes or you get some money back because there was a failure in production, the expenditure will change too. 

## Identities & associations
For View the name of the given Domain is a good identity, as it specifies the corresponding visualization of budget or expenditures or both. This gives a hint for the association. View can have more than one expenditure to visualize and expenditure can have more than just one view. Next to that there is also a unidirectional association between budget and view, because a budget can have more than just one view, but view can have just one budget to visualize, as budget should be set at the beginning of the year/month. A good identity for expenditure and budget is the time to which they are corresponding and also the category. 

## Aggregates
Budget and Visualization are changing over the year. Budget is mostly changing every month. So we declare a aggregate root Budget with one entity, which changes/adds/deletes the budget. In Visualization there is a aggregate root, which controls the data flow into its domain. After that it can apply some visualization based on that input. This means that the aggregate ViewCategorizer has the entity view. Given the expenses, which are immutable, because they are created just once, the expense domain has just an aggregate root with a value object. 

## Repositories
By looking at the repositories every aggregate needs a repository. But it is just the budget and the expense which needs to update the repositories. Therefore these two get a repository. The Visualization don't need to update or add/delete something in the repository. It can ask the budget and expense aggregate for the data in their repository. 
