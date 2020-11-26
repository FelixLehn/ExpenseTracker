# Domain Driven Design - Concept
In this post I apply Domain-Driven Design to my favorite pet project. The picture above contains the resulting model. The resulting code can be found at GitHub.

##My attempt on Domain-Driven design
As mentioned in my previous post I need to learn Domain-Driven Design for my new job. In this post I apply the things I learned till now to an application that gives me insight in my financial situation. The domain is very familiar to me as I used it before to learn new things. The application mainly tells me where I spent my money. Next to that I set yearly budgets on each category in the beginning of a year. During that year I will compare the budget against the actual situation to assess if I’m still on track. Ideally the application also incorporates some functionality to calculate my savings rate and some other metrics related to reaching financial independence.

##Ubiquitous language
Eric Evans’ book emphasizes the importance of the ubiquitous language. So let me try to define the ubiquitous language for this application.

To achieve financial insight the application needs to import and categorize financial transactions. I want to set budgets for a year and compare them to the actual amounts. Furthermore based on the actual numbers the savings rate and years till financial independence must be calculated. In order to calculate the years till financial independence there is something to assess my savings and investments.

The bold words seem fundamental concepts to me. These words should play a major role in my domain. Probably I miss a couple of concepts right now, but that is fine. I will refine the ubiquitous language later. The most interesting part of the application to me is the last part: calculating the metrics on FI. However these are a result. In order to achieve FI earlier there are two possibilities:

Increase your income
Reduce your spendings
The application will not help in getting more income. Getting insight in your expenses can help to see when budgets are exceeded and where expenses are high. So for now I first focus on categorizing financial transactions and creating budgets.

Please note that for my personal finances I don’t use double bookkeeping as it seems overkill. Next to that I ignore any cash transactions. Not categorizing cash transactions will not influence my insights much as I don’t use a lot of cash. Next to that keeping all receipts is too much of a burden to me.

##Entities versus value objects
After defining the ubiquitous language the next step in Domain-Driven Design is to try to make the model. Important parts of the model are the entities and value objects. As the focus is on categorizing and budgeting I find at least 3 objects of interest: Category, Transaction and Budget. To me a Category is an entity. Mainly because in time the amount of money spent in a Category will change via adding new transactions. Furthermore there must be a Budget more specifically a Budget per Category per year. Budgets are entities as pretty much anything can change in time.

If I look at Transaction I’m a bit in doubt. During the life cycle of my financial administration a transaction will not change. That is because they are originating in an external source: my bank. Next to that I’m only concerned about the values of a Transaction. If I need to make a guess I think I need an account number, a contra account, the date, the amount and the description of the Transaction. These fields are also the important ones in my naive Bayesian classifier to categorize my transactions. For now I make a choice to make a Transaction a value object. This might be revisited later.

##Identities & associations
For Category the name is a good identity. There is a unidirectional association from category to zero or more Transactions. Next to that there is a unidirectional association between a Budget and a Category. Because setting a Budget without being able to categorize real Transactions doesn’t make sense, it is not possible to have a Budget without a corresponding Category. Over the years there are many Budgets per Category, however per year there can be only 1. This means that for the identity of the Budget it is probably wise to include the year. To me combining the Category and a year seems a good choice as identity for the Budget.

##Aggregates
Time to define some aggregates in the model. Typically a Budget is created at the beginning of each year and Categories are created once (and maybe adjusted once in a while). However during the year I import and categorize my Transactions. For me this leads to a logical split. Making Budget an aggregate with only one entity. Category and Transactions are an aggregate as well. Category is the aggregate root. As Budget is a separate aggregate root I don’t want to include the Category as an object. I just want to have a reference to a Category through its identity. This has implications for the Budget and its identity. It identity is now made of a Category name and a year.

##Repositories
Time to choose the repositories. My first attempt is a repository per aggregate. Given the requirements this makes sense to me now. In the future I probably want to persist my data somehow. Maybe with a relational database, maybe an object database or maybe just plain old CSV files. For exploring and building the domain this is not relevant. Furthermore maybe some future feature(s) will give me more information what storage technology will suit my needs. For now I will just use an plain old java implementation of my repository, using the collection classes.

##Creation of aggregates
Creating a category is straight forward as there are no special requirements here. So a constructor will suffice. However for creating a Budget we need to make sure that there actually is a Category available. To check if a Category exists I need to find the Category by name using the CategoryRepository. I could make an association in Budget to that repository. However that seems bad practice. I think creating a BudgetFactory makes sense in this case.

##Conclusion
Given the small number of objects in the domain now I don’t find it necessary to split these classes among different modules yet. The model created seems to cover my basic needs of storing the budgets and categorize transactions. The complete design is shown below.
