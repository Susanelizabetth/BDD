Feature: Calculate multiple of the given parameters

  Scenario Outline: calculations
     Given the number <number>
     When calculates the result
     Then the result should be <result>
     
     Examples: Process
     | number         | result        |
     | 2              | 2             |
     | 4              | 4             |
     | 8              | 8             |
     | 3              | Tresss          |
     | 6              | Tresss          |
     | 9              | Tresss          |
     | 5              | Cincoo          |
     | 10             | Cincoo          |
     | 20             | Cincoo          |
     | 15             | TressCinco        |
     | 30             | TresssCincoo      |
     | 45             | TresssCincoo      |