"""AICelltype: Annotate cell type through AI/LLM/GPT"""

import requests
import re
import json
import os

from http import HTTPStatus
from dashscope import Generation
import dashscope

dashscope.api_key = os.environ.get('QWEN_KEY', '')
API_KEY = os.environ.get('API_KEY', '')
SECRET_KEY = os.environ.get('SECRET_KEY', '')


def aicelltype(tissue_name, gene_list, model='gpt4'):
    """
    Parameters
    ----------
    tissue_name
        In theory, issue_name can be any type of biological tissue.
    gene_list
        Identify one cell type for each row in gene_lt.
    model
        model should be chosen from ['gpt4', 'qwen-max', 'ERNIE-4.0'].
        gpt4: annotate cell type through gpt4 (default);
        qwen-max: annotate cell type through ali qwen model, QWEN_KEY needed, refer to https://help.aliyun.com/zh/dashscope/developer-reference/activate-dashscope-and-create-an-api-key for a key;
        ERNIE-4.0: annotate cell type through  baidu qianfan model, API_KEY and SECRET_KEY, refer to https://console.bce.baidu.com/qianfan/ais/console/applicationConsole/application for them.

    usage1:
        # gpt4 model
        issue_name = 'human prostate'
        gene_lt = [
            ['KLK3', 'KRT8', 'KLK2', 'MSMB', 'ACPP', 'KLK1', 'KLK4'],
            ['MMRN1', 'FLT4', 'RELN', 'CCL21', 'PROX1', 'LYVE1'],
            ['CD69', 'IL7R', 'CD3D', 'CD3E', 'CD3G', 'ACTA2', 'MYO1B', 'ACTA2', 'ANPEP', 'PDGFRB', 'CSPG4'],
            ['DDX49', 'LOC105371196', 'MTND1P30', 'LOC105373682', 'TAGLN2', 'ZNF836', 'ZNF677', 'COILP1']
        ]

        from AICelltype import aicelltype
        cell_lt = aicelltype(issue_name, gene_lt, model='gpt4')
        print(cell_lt)
    output1:
        ['Prostate Epithelial Cells', 'Lymphatic Endothelial Cells', 'T Cell and Myofibroblast', 'Unknown Cell Type']
        In result, you can get a list with four cell types which have the same order with parameter gene_list.

    usage2:
        # qwen-max model
        import os
        os.environ['QWEN_KEY'] = 'your QWEN_KEY'  # Add QWEN_KEY to environ, keep secret to yourself.

        from AICelltype import aicelltype
        cell_lt = aicelltype(tissue_name, gene_lt, model='qwen-max')
        print(cell_lt)
    output2:
        ['Prostate secretory epithelial cell', 'Lymphatic endothelial cell', 'Immune cell (likely T-cell) and smooth muscle cell mixture', 'Unknown cell type']

    usage3:
        # ERNIE-4.0 model
        import os
        os.environ['API_KEY'] = 'your AIP_KEY'  # Add API_KEY to environ, keep secret to yourself.
        os.environ['SECRET_KEY'] = 'your SECRET_KEY'  # Add SECRET_KEY to environ, keep secret to yourself.

        from AICelltype import aicelltype
        cell_lt = aicelltype(tissue_name, gene_lt, model='ERNIE-4.0')
        print(cell_lt)
    output3:
        ['Prostate glandular cells (or Prostate epithelial cells)', 'Lymphatic endothelial cells', 'T-cells (or T-lymphocytes)', 'Unknown cell type (or Possibly cancer-associated cells or Stromal cells; needs further investigation)']  # This model give more explaination.
    """
    if model == 'gpt4':
        cell_lt = gpt4(tissue_name, gene_list)
    elif model == 'qwen-max':
        cell_lt = qwen(tissue_name, gene_list)
    elif model == 'ERNIE-4.0':
        cell_lt = ernie(tissue_name, gene_list)
    else:
        print(f'error:model {model} no found, choose one from ["gpt4", "qwen-max", "ERNIE-4.0"]')
        return
    return cell_lt


def gpt4(tissue_name, gene_list):
    token_js = get_token()
    gene_str = '\n'.join([','.join(i) for i in gene_list])
    url = 'https://gq86p6-3000.csb.app/api/sydney'
    data = {
        "conversationId": token_js['conversationId'],
        "encryptedconversationsignature": token_js['encryptedconversationsignature'],
        "clientId": token_js['clientId'],
        "invocationId": 0,
        "conversationStyle": "Precise",
        "prompt": f"Identify cell types of {tissue_name} cells using the following markers. Identify one cell type for each row. Only print the cell type name without any markdown code. Some could be a mixture of multiple cell types. Some could be unknown cell types.\n{gene_str}",
        "allowSearch": "false",
        "context": ""
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        result = response.text
        print("success:", response.status_code)
        # print(result)
        regx = re.compile('"message":"(.*?)"', re.S)
        cellstr = re.findall(regx, result)[0]
        return cellstr.split('\\n')
    else:
        print(f"failed:{response.status_code}")
    return [''] * len(gene_list)

def get_token():
    url = 'https://gq86p6-3000.csb.app/api/create'
    response = requests.post(url, data={})
    return response.json()


def qwen(tissue_name, gene_list):
    gene_str = '\n'.join([','.join(i) for i in gene_list])
    input_msg = f'Identify cell types of {tissue_name} cells using the following markers. Identify one cell type for each row. Only provide the cell type name and nothing else without number before the output. Some could be a mixture of multiple cell types. Some could be unknown cell types.\n{gene_str}'
    # print(input_msg)
    messages = [{'role': 'user', 'content': input_msg}]
    response = Generation.call("qwen-max",
                               messages=messages,
                               result_format='message',
                              )
    if response.status_code == HTTPStatus.OK:
        # print(response)
        cellstr= response['output']['choices'][0]['message']['content']
        cell_lt = cellstr.split('\n')
        return cell_lt
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))
        return [''] * len(gene_list)


def ernie(tissue_name, gene_list):
    gene_str = '\n'.join([','.join(i) for i in gene_list])
    input_msg = f'Identify cell types of {tissue_name} cells using the following markers. Identify one cell type for each row. Only provide the cell type name and nothing else without number before the output. Some could be a mixture of multiple cell types. Some could be unknown cell types.\n{gene_str}'
    # print(input_msg)
    # print('token', get_access_token())
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-4.0-8k-preview?access_token=" + get_access_token()
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": input_msg
            },
        ],
        "disable_search": False,
        "enable_citation": False
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        # print('response', response.text)
        # print('\n')
        res_js = response.json()
        cell_lt = res_js['result'].split('\n')[:len(gene_list)]
        return cell_lt
    else:
        print(f"failed:{response.status_code}")
        return [''] * len(gene_list)


def get_access_token():
    """
    use AK, SK generate(Access Token)
    :return: access_token or None(if wrong)
    """
    # print('API_KEY:', API_KEY, 'SECRET_KEY:', SECRET_KEY)
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

