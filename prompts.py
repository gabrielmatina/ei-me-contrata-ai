def resumo_prompt(text):
    return f"""
    Aqui está o resumo do perfil do LinkedIn de um profissional:
    {text}

    Avalie a clareza e objetividade desse resumo. Ele comunica bem os objetivos profissionais e as habilidades principais? 
    Dê sugestões para melhorá-lo, se necessário.
    """

def experiencias_prompt(text):
    return f"""
    Aqui estão as experiências profissionais do usuário no LinkedIn:
    {text}

    Avalie a clareza das descrições, identificando pontos fortes e fracos. 
    As experiências são coerentes com a área de atuação? Há algo que poderia ser melhor descrito?
    """

def habilidades_prompt(text):
    return f"""
    Aqui estão as habilidades listadas pelo usuário no LinkedIn:
    {text}

    Analise se as habilidades são relevantes para a área desejada. Há alguma habilidade essencial que está faltando?
    """

def certificacoes_prompt(text):
    return f"""
    Aqui estão as certificações e formações acadêmicas do usuário no LinkedIn:
    {text}

    As certificações são relevantes para a área de atuação? Quais cursos ou certificações poderiam ser adicionados para fortalecer o perfil?
    """

def sugestoes_melhoria_prompt(text):
    return f"""
    Baseado em todas as informações do perfil do LinkedIn abaixo:
    {text}

    Quais melhorias podem ser feitas no perfil para torná-lo mais atraente para recrutadores? 
    Sugira palavras-chave estratégicas que aumentariam a visibilidade do perfil.
    """
