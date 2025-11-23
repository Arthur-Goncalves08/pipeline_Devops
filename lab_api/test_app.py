import unittest
from app import app
import werkzeug
import json

# Patch temporário para adicionar o atributo '__version__' em werkzeug
if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase):
    """
    Conjunto de testes unitários para as funcionalidades da API Flask.
    """
    @classmethod
    def setUpClass(cls):
        # Criação do cliente de teste para fazer requisições
        cls.client = app.test_client()
        cls.access_token = None

    # 1. Teste de Estado e Integridade (GET /items)
    def test_get_items_integrity(self):
        """
        Testa se a rota '/items' retorna status 200 e se o payload JSON
        contém a lista exata de itens esperada.
        """
        print("\n--- Executando Teste 1: Integridade da Rota /items ---")
        response = self.client.get('/items')
        
        # Verifica o código de status
        self.assertEqual(response.status_code, 200)
        
        # Verifica o conteúdo da resposta JSON
        expected_items = ["item1", "item2", "item3"]
        self.assertEqual(response.json['items'], expected_items)
        print("Teste 1 OK: Status 200 e lista de itens correta.")

    # 2. Teste de Interação de Segurança (Falha em /protected)
    def test_protected_route_unauthorized(self):
        """
        Testa o cenário negativo: verifica se a rota protegida retorna 401 
        quando nenhum token é fornecido.
        """
        print("\n--- Executando Teste 2: Falha de Autorização ---")
        response = self.client.get('/protected')
        
        # Deve retornar 401 Unauthorized
        self.assertEqual(response.status_code, 401)
        print("Teste 2 OK: Status 401 retornado para token ausente.")

    # 3. Teste de Interação de Segurança (Sucesso em /protected)
    def test_protected_route_with_valid_token(self):
        """
        Testa o fluxo completo: login para obter token e acesso à rota 
        protegida com sucesso.
        """
        print("\n--- Executando Teste 3: Sucesso de Autorização (Fluxo) ---")
        
        # PASSO A: Obter o token (Login)
        login_response = self.client.post('/login')
        self.assertEqual(login_response.status_code, 200)
        
        # Extrai o token
        self.access_token = login_response.json.get('access_token')
        self.assertIsNotNone(self.access_token)
        print("Sub-teste A OK: Token obtido com sucesso.")

        # PASSO B: Acessar a rota protegida com o token
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        protected_response = self.client.get('/protected', headers=headers)
        
        # Verifica o código de status e o payload da rota protegida
        self.assertEqual(protected_response.status_code, 200)
        self.assertEqual(protected_response.json, {"message": "Protected route"})
        print("Sub-teste B OK: Acesso à rota protegida realizado com sucesso.")


if __name__ == '__main__':
    # A linha abaixo permite que você veja a saída dos prints de cada teste
    unittest.main(verbosity=2)