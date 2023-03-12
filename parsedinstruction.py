
#class for the breakdown of each step/instruction. Holds:
#cooking action - what process you need to do in that step
#quantity - how much of the ingredients do you need in that step
#time = how long you need to do the cooking action
#ingredients - the ingredients needed in that step
#tools - the cookware/kitchenware needed for that step
class parsedInstruction:
    def __init__(self, ingredient, cookingAction, quantity, time, tool):
        self.cookingAction = cookingAction
        self.quantity = quantity
        self.time = time
        self.ingredient = ingredient
        self.tool = tool


   