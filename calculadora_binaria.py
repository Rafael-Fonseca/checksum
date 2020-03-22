class CalculadoraBinaria():

    def converte_bits_sequencia_binaria(self, bits_iteraveis):
        sequencias_binaria = []
        for iteravel in bits_iteraveis:
            sequencias_binaria.append(iteravel[2:])
        return sequencias_binaria

    def prepara_soma(self, sequencia_binaria_1, sequencia_binaria_2, tamanho_maximo=16):

        if len(sequencia_binaria_1) > tamanho_maximo or len(sequencia_binaria_2) > tamanho_maximo:
            return print('erro, alguma das sequências binárias apresenta mais que 16 dígitos.')

        try:
            int(sequencia_binaria_1)
            int(sequencia_binaria_2)
        except ValueError:
            return print('erro, alguma das sequências binárias apresenta caracteres inválidos.')

        for bit in sequencia_binaria_1:
            if int(bit) < 0 or int(bit) > 1:
                return print('erro, a primeira sequência binária apresenta caracteres inválidos.')

        for bit in sequencia_binaria_2:
            if int(bit) < 0 or int(bit) > 1:
                return print('erro, a segunda sequência binária apresenta caracteres inválidos.')

        tamanho_soma = ''
        if len(sequencia_binaria_1) > len(sequencia_binaria_2):
            for dif_tamanho in range(0,len(sequencia_binaria_1)-len(sequencia_binaria_2)):
                tamanho_soma = '0'+ tamanho_soma

            sequencia_binaria_2 = tamanho_soma + sequencia_binaria_2

        elif len(sequencia_binaria_1) < len(sequencia_binaria_2):
            for dif_tamanho in range(0, len(sequencia_binaria_2) - len(sequencia_binaria_1)):
                tamanho_soma = '0' + tamanho_soma

            sequencia_binaria_1 = tamanho_soma + sequencia_binaria_1

        else:
            pass

        return self.soma_complemento_1(sequencia_binaria_1, sequencia_binaria_2, tamanho_maximo=16)

    def soma_complemento_1(self, sequencia_binaria_1, sequencia_binaria_2, tamanho_maximo=16):
        # print('seq 1: ', sequencia_binaria_1)
        # print('seq 2: ', sequencia_binaria_2, '\n')
        resultado = ''
        carry = 0
        for bit in range(15, -1, -1):

            try:
                sequencia_binaria_1[bit]
            except IndexError:
                continue

            resultado_parcial = int(sequencia_binaria_1[bit]) + int(sequencia_binaria_2[bit]) + carry
            '''
            print('bit: ', bit)
            print('seq1[bit]: ', sequencia_binaria_1[bit])
            print('seq2[bit]: ', sequencia_binaria_2[bit])
            print('carry antes', carry, '\n')
            print('resultado parcial: ', resultado_parcial)
            '''

            if resultado_parcial == 2:
                resultado = '0' + resultado
                carry = 1
                '''
                print('resultado', resultado)
                print('carry', carry)
                '''

            elif resultado_parcial == 3:
                resultado = '1' + resultado
                carry = 1
                '''
                print('resultado', resultado)
                print('carry', carry)
                '''

            else:
                resultado = str(resultado_parcial) + resultado
                carry = 0
                '''
                print('resultado', resultado)
                print('carry', carry)
                '''

            if bit == 0 and carry == 1:
                resultado = '1' + resultado

            # print('\n === Próximo bit === ')

        if len(resultado) > tamanho_maximo:
            resultado = self.soma_complemento_1(resultado[1:], '0000000000000001')

        # print('\nresultado final: ', resultado)

        return resultado

    def complemento_1(self, sequencia_binaria):
        complemento = ''
        for bit in sequencia_binaria:
            if bit == '0':
                complemento = complemento + '1'
            else:
                complemento = complemento + '0'

        return complemento

    def checksum(self, sequencia_binaria_1, sequencia_binaria_2, tamanho_maximo=16):
        resultado = self.prepara_soma(sequencia_binaria_1, sequencia_binaria_2, tamanho_maximo)
        return self.complemento_1(resultado)
