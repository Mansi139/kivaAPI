import ast
from graphqlclient import GraphQLClient

client = GraphQLClient('http://api.kivaws.org/graphql')

result = client.execute('''
{
  loans(filters: {status: fundRaising}, sortBy: expiringSoon) {
    totalCount
    values {
      id
      name
      plannedExpirationDate
      loanAmount
      loanFundraisingInfo{
        fundedAmount
      }
      updates{
        values{
          permalink
        }
      }
    }
  }
}

''')

#print(result)

#aggregate results

ast.literal_eval(result)
result = ast.literal_eval(result)
result = result["data"]["loans"]["values"]

total = 0
for x in result:
	total = total +  float(x["loanAmount"])	

print("Total amount needed to fund all the loans: " ,total)

