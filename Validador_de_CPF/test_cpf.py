from valida_cpf import validacpf
import unittest


class ValidaCpfTest(unittest.TestCase):
    def test_cpf_1(self):
        self.assertEqual(validacpf(12345678909), 'CPF Valido !!!')

    def test_cpf_2(self):
        self.assertEqual(validacpf('ssssssssss'), 'CPF Invalido Deve Conter 11 Números')

    def test_cpf_3(self):
        self.assertEqual(validacpf('123nh.456df.789--09aa'), 'CPF Valido !!!')

    def test_cpf_4(self):
        self.assertEqual(validacpf('123.456.789.01'), 'CPF Invalido')

    def test_cpf_5(self):
        self.assertEqual(validacpf('123.456.788-0b'), 'CPF Invalido Deve Conter 11 Números')

    def test_cpf_6(self):
        self.assertEqual(validacpf('123.456.788-041'), 'CPF Invalido Deve Conter 11 Números')


if __name__ == '__main__':
    unittest.main()