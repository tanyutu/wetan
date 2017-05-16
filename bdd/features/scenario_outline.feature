
Feature: scenario outline
  Scenario Outline: check the equal letters
    Given: I have a letter
    When I input a letter <letter>
    Then the input letter is Equal to <target_letter>
    Examples: Testing
    |letter|target_letter|
    |a     |a            |
    |C     |C            |




