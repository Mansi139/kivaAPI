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
