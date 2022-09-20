import logging
import json
from jira import JIRA
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    username="amit.894@gmail.com"
    token="NotMyBitCoin"
    options = {
        'server': 'https://amit894.atlassian.net/'}
    jira = JIRA(
            basic_auth=(username,token),options=options)

    jira.create_issue(summary="Third Issue", description="Yes this is JIRA", issuetype={'name': 'Task'}, project='MB',
                                  assignee={'name': 'amitraj'})
    return func.HttpResponse(
        json.dumps({
            'method': req.method,
            'url': req.url,
            'headers': dict(req.headers),
            'params': dict(req.params),
            'get_body': req.get_body().decode()
        })
    )