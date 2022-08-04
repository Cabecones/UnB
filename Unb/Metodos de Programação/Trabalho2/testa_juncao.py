import juncao

caminhos = ['file1.txt', 'file2.txt']

# testar se caminho existe
def test_verifica_arquivo():
    assert juncao.verifica_arquivo(caminhos) == True
    assert juncao.verifica_arquivo(['file7.txt']) == False

# testar se o arquivo é vazio
def test_verifica_vazio():
    assert juncao.verifica_vazio(caminhos) == False
    assert juncao.verifica_vazio(['filetest.txt']) == True

#testar a junção dos arquivos
def test_juncao_arquivos():
    juncao.juncao(caminhos)
    with open('final.txt', 'r') as arquivo:
        assert arquivo.read() == '1\n2\n3\n4\n5\n6\n7\n8\n9\n'

#testar a junção dos arquivos com um caminho inválido
def test_juncao_arquivos_invalido():
    caminhos = ['file17.txt', 'file1.txt', 'filetest.txt']
    assert juncao.juncao(caminhos) == 'Impossível criar arquivo final.txt'

#juncao dos arquivos com um arquivo vazio
def test_juncao_arquivos_vazio():
    caminhos = ['filetest.txt', 'file1.txt', 'file2.txt']
    assert juncao.juncao(caminhos) == 'Impossível criar arquivo final.txt'