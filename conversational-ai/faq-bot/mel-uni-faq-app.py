from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient

def main():
    try:
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')
        ai_project_name = os.getenv('QA_PROJECT_NAME')
        ai_deployment_name = os.getenv('QA_DEPLOYMENT_NAME')

        credential = AzureKeyCredential(ai_key)
        ai_client = QuestionAnsweringClient(endpoint=ai_endpoint, credential=credential)

        user_question = ''
        while True:
            user_question = input('\nQuestion:\n')
            if user_question.lower() == "quit":
                break
            
            response = ai_client.get_answers(question=user_question, project_name=ai_project_name, deployment_name=ai_deployment_name)

            for answer in response.answers:
                print("Answer: {}".format(answer.answer))
                print("Confidence: {}".format(answer.confidence))
                print("Source: {}".format(answer.source))
    
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()