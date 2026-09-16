from pydantic import BaseModel


class CreateCampaign(
    BaseModel
):
    gov_rep_id: int

    campaign_name: str

    description: str

    start_date: str

    end_date: str

    target_state: str

    target_district: str