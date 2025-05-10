from diagrams.programming.flowchart import Action, Decision
from diagrams import Diagram


with Diagram("Premium First Flow", show=False):
    # Start
    start = Action("Start")

    # Websites PDP
    user_input = Action("Premium First CTA")

    # Check Premium Status???? cart to dashboard navigation where siteID is required
    check_premium_status = Decision("Check Premium Status")

    # Premium User Flow - through navigation service
    premium_user_flow = Action("Navigate to the Plan Picker Page")

    # Non-Premium User Flow
    non_premium_user_flow = Action("Same as before")

    # End
    end = Action("End")

    # Define the flow
    start >> user_input >> check_premium_status
    check_premium_status >> premium_user_flow
    check_premium_status >> non_premium_user_flow
    premium_user_flow >> end
    non_premium_user_flow >> end