/* ---------------Variáveis--------------*/
var listaFuncionarios = {
	
	funcionarios: [],

	exibeLista: function(){
		console.log('Funcionários cadastrados:')
		for (var i=0; i < this.funcionarios.length; i++){
			console.log(this.funcionarios[i].nome);
		}
	},

	adicionaFuncionario: function(nome,cargo,cor,sexo){
		
		this.funcionarios.push({
			nome:nome,
			cargo:cargo,
			cor:cor,
			sexo:sexo,
			gravidez:false
		});
		this.exibeLista()
	}
}



var displayFuncionariosButton = document.getElementById("displayFuncionariosButton");

displayFuncionariosButton.addEventListener('click', function(){
	funcionario.displayFuncionario();
});

var handlers = {
	displayFuncionarios: function(){
		funcionario.displayFuncionario()
	},

	addFuncionario: function(){
		var addNomeInput = document.getElementById('addNomeInput')
		var addCargoInput = document.getElementById('addCargoInput')
		var addCorInput = document.getElementById('addCorInput')
		var addSexoInput = document.getElementById('addSexoInput')

		listaFuncionarios.adicionaFuncionario(addNomeInput.value, addCargoInput.value, addCorInput.value, addSexoInput.value);

		addNomeInput.value='';
		addCargoInput.value ='';
		addCorInput.value ='';
		addSexoInput.value ='';

		view.displayFuncionarios();

	}
};

var view = {
	displayFuncionarios(){
		var funcUl = document.querySelector('ul');
		funcUl.innerHTML=''
		for (var i=0; i<listaFuncionarios.funcionarios.length;i++){
			var funcLi = document.createElement('li');
			funcLi.textContent = listaFuncionarios.funcionarios[i].nome;
			funcUl.appendChild(funcLi);
		}
	}
};









