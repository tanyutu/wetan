
Feature: scenario outline
  Scenario Outline: : check the equal letters
    Given: I have a letter
    When I input a letter <letter>
    Then the input letter is Equal to <target_letter>
    Examples: Testing
    |letter|target_letter|
    |a     |b            |
    |C     |C            |



#For the first test data should be failed
#But the result show as
#1 feature passed, 0 failed, 0 skipped
#2 scenarios passed, 0 failed, 0 skipped
#4 steps passed, 0 failed, 0 skipped, 0 undefined

