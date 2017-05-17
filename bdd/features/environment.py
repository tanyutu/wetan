def before_feature(context, feature):
    context.first_output = 1
def before_scenario(context, scenario):
    context.second_output = 2


    #before_feature(context, feature), after_feature(context, feature)
# These run before and after each feature file is exercised.

# before_scenario(context, scenario), after_scenario(context, scenario)
# These run before and after each scenario is run.
