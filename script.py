import ast
from graphqlclient import GraphQLClient

client = GraphQLClient('http://api.kivaws.org/graphql')

result = client.execute('''
 {
   loans(filters: {status: fundRaising}, sortBy: amountLeft) {
     totalCount
     values {
       name
       plannedExpirationDate
       loanAmount
     }
 }
}
''')

print(result)

#aggregate results

ast.literal_eval(result)
result = ast.literal_eval(result)
result = result["data"]["loans"]["values"]

total = 0
for x in result:
	total = total +  float(x["loanAmount"])	

print("total is: " ,total)

