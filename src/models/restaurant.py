class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    # 1- Melhoria: correção para retornar os textos da descrição do restaurante
    # 2- Melhoria: correção na chamada do restaurant_name
    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""
        print(f"Esse restaurante chama {self.restaurant_name} e serve {self.cuisine_type}.")
        print(f"Esse restaurante está servindo {self.number_served} consumidores desde que está aberto.")

    # 3- Melhoria: Alterado o valor do 'self.open' de False para True
    # 4- Melhoria: Alterado o valor do 'number_served' de -2 para 0
    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            self.open = True
            self.number_served = 0
            print(f"{self.restaurant_name} agora está aberto!")
        else:
            print(f"{self.restaurant_name} já está aberto!")

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            self.number_served = 0
            print(f"{self.restaurant_name} agora está fechado!")
        else:
            print(f"{self.restaurant_name} já está fechado!")

    # 5- Melhoria: Após definir o numero total de pessoas atendidas foi adicionado um retorno informando o seu valor
    # 6- Melhoria: Adicionado retorno do metodo, quando for informado uma valor que não seja um numero
    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        try:
            total_customers = int(total_customers)
            if self.open:
                self.number_served = total_customers
                print(f"Esse restaurante está servindo {self.number_served} consumidores desde que está aberto.")
            else:
                print(f"{self.restaurant_name} está fechado!")
        except ValueError:
            print("Por favor, informe um valor válido (número inteiro) para o número de clientes atendidos.")

    # 6- Melhoria: Alterado de = para +=
    # 7- Melhoria: Após aumentar o numero total de pessoas atendidas foi adicionado um retorno informando o seu valor
    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        try:
            more_customers = int(more_customers)
            if self.open:
                self.number_served += more_customers
                print(f"Esse restaurante está servindo {self.number_served} consumidores desde que está aberto.")
            else:
                print(f"{self.restaurant_name} está fechado!")
        except ValueError:
            print("Por favor, informe um valor válido (número inteiro) para o número de clientes atendidos.")
