#The step decorator matches the step to any step type, “given”, “when” or “then”.
#The “and” and “but” step types are renamed internally to take the preceding step’s keyword
#(so an “and” following a “given” will become a “given” internally and use a “give” decorated step).

Feature: How to use and but in scenario
    Scenario: same to show the usage of and but in scenario
     Given How to use the and but
      When when I input a when
      And this when can be replaced by but
      Then when i input a then
      But this then can be replaced by and