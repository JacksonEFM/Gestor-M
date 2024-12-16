def sec():
    sections = {

    "4.2": [
        "As senhas fornecidas pelo fabricante não podem ser fracas, seguindo os critérios de segurança. Definição de senha fraca: senha que não atende simultaneamente os seguintes critérios:  a) possuir, no mínimo, 8 caracteres; -- b) conter, pelo menos, uma letra maiúscula, uma letra minúscula, um número e um caractere especial (Se atender ao item 4.4, selecione este campo também)."
    ],

    "4.3": [
        "a) As senhas iniciais não podem ser iguais para todos os dispositivos fabricados. -- Verificar se dois dispositivos possuem a mesma senha inicial (Se atender ao item 4.4, selecione este campo também).",
        "b) As senhas iniciais não podem ser baseadas em informações fáceis de descobrir, como endereços MAC (Se atender ao item 4.4, selecione este campo também).",
        "c) Não é permitido usar senhas em branco ou senhas fracas (Se atender ao item 4.4, selecione este campo também)."
    ],

    "4.4": [
        "Alternativamente ao 4.2 e 4.3. O dispositivo pode exigir que o usuário altere a senha padrão na primeira vez que for usado ou após um reset (Se o 4.2 e o 4.3 forem atendidos, selecione este campo também).",
        "4.4.1: Se for o caso anterior. O dispositivo só pode ser usado após o usuário definir novas senhas que atendam aos requisitos de segurança (Se o 4.2 e o 4.3 forem atendidos, selecione este campo também)."
    ],

    "4.5": [
        "As senhas devem estar em uma etiqueta no dispositivo e devem ser restauradas para as configurações padrão após um reset."
    ],


    "5.2": [
        "a) Não deve ser permitido usar senhas em branco ou fracas. Definição de senha fraca: senha que não atende simultaneamente os seguintes critérios:  a) possuir, no mínimo, 8 caracteres; -- b) conter, pelo menos, uma letra maiúscula, uma letra minúscula, um número e um caractere especial.",
        "c) O manual do produto deve informar o número mínimo e máximo de caracteres permitidos para as senhas e as regras para criá-las."
    ],

    "5.3": [
        "O dispositivo deve verificar se as senhas definidas pelo usuário são fortes e não comumente usadas. Deve utilizar um dicionario de senhas.",
        "5.3.1: O método de verificação deve ser informado à autoridade responsável pela segurança do produto. (O dicionario utilizado deve ser informado ao laboratório)."
    ],

    "6.1": [
        "a) O dispositivo deve se proteger contra ataques de força bruta (tentativas repetidas de adivinhar a senha).",
        "b) O dispositivo não pode usar credenciais, senhas ou chaves fixas (hard-coded). Solicitar código fonte caso não enviado.",
        "c) As senhas e chaves de acesso devem ser protegidas com criptografia ou hashing adequados. Métodos que não são considerados seguros incluem:"
            " ---> MD5 (considerado vulnerável a colisões e ataques de força bruta)."
            " ---> SHA-1 (considerado fraco para criptografia e assinaturas digitais)."
            " ---> Criptografia SSL 2.0 e SSL 3.0 (obsoletos e vulneráveis a ataques).",
        "d) O dispositivo deve encerrar sessões inativas automaticamente após um certo período.",
        "e) O dispositivo deve desabilitar serviços desnecessários para reduzir os riscos de segurança. (Verificar quais portas estão abertas e comenta-las abaixo) Link de software de verificação https://drive.google.com/file/d/1mbBrFqPrW9qVcl85yJ0gkPqRLkBalKIO/view?usp=sharing",
        "f) O usuário deve poder desabilitar funcionalidades ou serviços que não são essenciais."
    ],

    "6.2": [
        "Se imlementado no produto. O sistema de recuperação de senha deve ser seguro para evitar roubo de credenciais.",
        "6.2.1: O método de recuperação de senha deve ser informado à autoridade responsável pela segurança do produto. O método deve estar presente no manual."
    ]
    }
    return sections
