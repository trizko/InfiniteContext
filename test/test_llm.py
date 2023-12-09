from llm import LLM

def test_llm_token_count():
    llm = LLM(api_key="")
    
    token_count = llm.num_tokens([
        {'role': 'user', 'content': 'hi, how are you?'}
    ])
    assert token_count == 13
    
    token_count = llm.num_tokens([
        {'role': 'user', 'content': 'hi, how are you?'},
        {'role': 'assistant', 'content': "Hello! I'm just a computer program, so I don't have feelings, but I'm here and ready to assist you with any questions or tasks you have. How can I help you today?"},
        {'role': 'user', 'content': 'oh sorry.'}
    ])
    assert token_count == 64
    
    token_count = llm.num_tokens([
        {'role': 'assistant', 'content': "Hello! I'm just a computer program, so I don't have feelings, but I'm here and ready to assist you with any questions or tasks you have. How can I help you today?"},
        {'role': 'user', 'content': 'oh sorry.'},
        {'role': 'assistant', 'content': "No need to apologize! If there's anything you're curious about or need assistance with, feel free to ask me. I'm here to help!"},
        {'role': 'user', 'content': 'thank you.'}
    ])
    assert token_count == 95
