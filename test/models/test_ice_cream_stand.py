import pytest

from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    @pytest.fixture
    def setup_ice_cream_stand(self):
        return IceCreamStand('Kibon', 'sorvetes', ['chocolate', 'morango', 'creme'])

    @pytest.fixture
    def setup_ice_cream_stand_no_estoque(self):
        return IceCreamStand('Kibon', 'sorvetes', [])

    @pytest.mark.parametrize('result',
                             ['\nNo momento temos os seguintes sabores de sorvete disponíveis:'
                              '\n\t-chocolate\n\t-morango\n\t-creme\n'])
    def test_flavors_available(self, setup_ice_cream_stand, result, capsys):
        # Setup
        sorveteria = setup_ice_cream_stand
        resultado_esperado = result

        # Chamada
        sorveteria.flavors_available()
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize('result', ['Estamos sem estoque atualmente!\n'])
    def test_flavors_available_no_estoque(self, setup_ice_cream_stand_no_estoque, result, capsys):
        # Setup
        sorveteria = setup_ice_cream_stand_no_estoque
        resultado_esperado = result

        # Chamada
        sorveteria.flavors_available()
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize('flavor, result', [('chocolate', 'Temos no momento chocolate!\n'),
                                                ('', 'Por favor, informe um sabor válido.\n'),
                                                ('menta', 'Não temos no momento menta!\n')])
    def test_find_flavor(self, setup_ice_cream_stand, flavor, result, capsys):
        # Setup
        sorveteria = setup_ice_cream_stand
        resultado_esperado = result

        # Chamada
        sorveteria.find_flavor(flavor)
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize('flavor, result', [('chocolate', 'Estamos sem estoque atualmente!\n'),
                                                ('', 'Estamos sem estoque atualmente!\n'),
                                                ('menta', 'Estamos sem estoque atualmente!\n')])
    def test_find_flavor_no_estoque(self, setup_ice_cream_stand_no_estoque, flavor, result, capsys):
        # Setup
        sorveteria = setup_ice_cream_stand_no_estoque
        resultado_esperado = result

        # Chamada
        sorveteria.find_flavor(flavor)
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize('flavor, result', [('menta', 'menta adicionado ao estoque!\n'),
                                                ('morango', 'morango já disponível!\n'),
                                                ('', 'Por favor, informe um sabor válido.\n')])
    def test_add_flavor(self, setup_ice_cream_stand, flavor, result, capsys):
        # Setup
        sorveteria = setup_ice_cream_stand
        resultado_esperado = result

        # Chamada
        sorveteria.add_flavor(flavor)
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize('flavor, result', [('menta', 'menta adicionado ao estoque!\n'),
                                                ('', 'Por favor, informe um sabor válido.\n')])
    def test_add_flavor_no_estoque(self, setup_ice_cream_stand_no_estoque, flavor, result, capsys):
        # Setup
        sorveteria = setup_ice_cream_stand_no_estoque
        resultado_esperado = result

        # Chamada
        sorveteria.add_flavor(flavor)
        captured = capsys.readouterr()
        resultado = captured.out

        # Avaliação
        assert resultado == resultado_esperado
