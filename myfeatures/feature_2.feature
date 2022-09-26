Feature: Scenario outline

Scenario Outline: Scene Outline Test
    Given: there are <start> cucumbers
    When: I deposit <deposit> cucumbers
    And: I withdraw  <withdraw> cucumbers
    Then: I should have <end> cucumbers

    Examples:
    | start | deposit | withdraw | end |
    | 12    | 5       | 7        | 10  |
    | 10    | 5       | 20       | 25  |
    | 10    | 5       | 2        | 13  |
    | 20    | 10      | 5        | 25  |
    | 30    | 15      | 10       | 35  |
