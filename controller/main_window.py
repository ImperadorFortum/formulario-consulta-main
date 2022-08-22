from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView
from PyQt5 import uic

from model.consulta import Consulta, Editar
from model.consulta_dao import ConsultaDAO

FILE_UI = 'view/main_window.ui'


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(FILE_UI, self)

        self.addBtn.clicked.connect(self.add)
        self.editBtn.clicked.connect(self.edit)
        self.delBtn.clicked.connect(self.delete)

        self.tabela.horizontalHeader().setStretchLastSection(True)
        self.tabela.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

        self.loadData()

    def loadData(self):
        listaCon = ConsultaDAO.selectAll()
        for c in listaCon:
            self.addTableWidget(c)

    def add(self):
        nome = self.nome.text()
        email = self.email.text()
        telefone = self.telefone.text()
        data = self.data.text()
        estado = self.estado.currentText()
        descricao = self.descricao.text()
        id = self.id.text() 

        novaConsulta = Consulta(-1, nome, email, telefone,
                                data, estado, descricao)
        
        id = ConsultaDAO.add(novaConsulta)
        novaConsulta.id = id

        self.addTableWidget(novaConsulta)
        
        self.nome.clear()
        self.email.clear()
        self.telefone.clear()
        self.descricao.clear()

    def edit(self):
        lineSel = self.tabela.currentRow()
        id = self.tabela.item(lineSel, 0)
        n_nome = self.tabela.item(lineSel,1) 
        n_email =self.tabela.item(lineSel,2)
        n_telefone = self.tabela.text(lineSel,3)
        n_data = self.tabela.text(lineSel,4)
        n_estado = self.tabela.text(lineSel,5)
        n_descricao = self.tabela.text(lineSel,6)
        
        
        n_nome = self.nome.text()
        n_email = self.email.text()
        n_telefone = self.telefone.text()
        n_data = self.data.text()
        n_estado = self.estado.currentText()
        n_descricao = self.descricao.text()

        edit = Consulta(id, n_nome, n_email, n_telefone,
                        n_data, n_estado, n_descricao)

        self.edicao(edit)
        ConsultaDAO.edit(edit)
        
        self.id.clear()
        self.nome.clear()
        self.email.clear()
        self.telefone.clear()
        self.descricao.clear()

    def delete(self):
        # pega a linha 
        lineSel = self.tabela.currentRow()

        item = self.tabela.item(lineSel,0) 
        id = item.text()
        print(id)
        # remove do banco
        ConsultaDAO.delete(id) 
        # remove a linha 
        self.tabela.removeRow(lineSel)

   
    def addTableWidget(self, c: Consulta):
        line = self.tabela.rowCount()
        self.tabela.insertRow(line)
        
        nome = QTableWidgetItem(str(c.id))
        email = QTableWidgetItem(c.email)
        tell = QTableWidgetItem(c.telefone)
        data = QTableWidgetItem(c.data)
        estado = QTableWidgetItem(c.estado)
        descricao = QTableWidgetItem(c.descricao)

        self.tabela.setItem(line, 0, nome)
        self.tabela.setItem(line, 1, email)
        self.tabela.setItem(line, 2, tell)
        self.tabela.setItem(line, 3, data)
        self.tabela.setItem(line, 4, estado)
        self.tabela.setItem(line, 5, descricao)

    def edicao(self, c: Editar):
        lineSel = self.tabela.currentRow()
        n_nome = QTableWidgetItem(c.nome)
        n_email = QTableWidgetItem(c.email)
        n_telefone = QTableWidgetItem(c.telefone)
        n_data = QTableWidgetItem(c.data)
        n_estado = QTableWidgetItem(c.estado)
        n_descricao = QTableWidgetItem(c.descricao)

        self.tabela.setItem(lineSel, 0, n_nome)
        self.tabela.setItem(lineSel, 1, n_email)
        self.tabela.setItem(lineSel, 2, n_telefone)
        self.tabela.setItem(lineSel, 3, n_data)
        self.tabela.setItem(lineSel, 4, n_estado)
        self.tabela.setItem(lineSel, 5, n_descricao)
