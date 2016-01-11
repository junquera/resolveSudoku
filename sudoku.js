var sudoku = [
 			0, 0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0, 0,
			0, 0, 0, 0, 0, 0, 0, 0, 0
		];

function bt(i){
      if(compruebaTodo() == 1){
            return 1;
      }
      for(var n = i; n < sudoku.length; n++){
            if(sudoku[n] != 0){
                  continue;
            } else {
                  for(var m = 1; m < 10; m++){
                        sudoku[n] = m;
                        if(comprueba(n) == -1){
                          sudoku[n] = 0;
                          continue;
                        }
                        valor = bt(n+1);
                        if (valor == -1){
                              sudoku[n] = 0;
                        } else if (valor == 1){
                              return 1;
                        }
                  }
                  return -1;
            }
      }
}

function compruebaTodo(){
      var coincidencias = 0;
      for(var i = 0; i < sudoku.length; i++){
            var valor = comprueba(i);
            if(valor == -1){
                  return -1
            } else if(valor == 1){
                  coincidencias += 1
            }
      }
      return coincidencias == sudoku.length? 1 : 0;
}

function comprueba(i){
      var aux = i;
      while(aux%9 > 0){
            aux -= 1;
      }

      var coincidenciasH = 0;
      for(var x = aux; x < aux + 9; x++){
            if(sudoku[x] == 0 ){
                  continue;
            } else if(sudoku[x] == sudoku[i] && i != x){
                  return -1;
            } else if(sudoku[x] != 0){
                  coincidenciasH += 1;
            }
      }

      var valoresV = new Array();
      for(var x = 0; x < 9; x++){
            valoresV.push(9*x + i%9);
      }

      var coincidenciasV = 0;
      for(var x = 0; x < valoresV.length; x++){
            if( sudoku[valoresV[x]] == sudoku[i] && i != valoresV[x]){
                  return -1;
            } else if( sudoku[valoresV[x]] != 0){
                  coincidenciasV += 1;
            }
      }

      var posicion0C = i;
      while( posicion0C % 3 !=0){
            posicion0C -= 1;
      }

      var mod = posicion0C%27;
      while( mod != 0 && mod != 3 && mod != 6){
            posicion0C -= 9;
            mod = posicion0C%27;
      }
      var valoresC =  new Array();
      for(var x = 0; x < 3; x++){
            for(var y = 0; y < 3; y++){
                  valoresC.push( 9 * x + posicion0C + y );
            }
      }
      var coincidenciasC = 0;
      for(var x = 0; x < valoresC.length; x++){
            if( sudoku[valoresC[x]] == sudoku[i] && i!=valoresC[x]){
                  return -1
            }
            if( sudoku[valoresC[x]] != 0){
                  coincidenciasC += 1
            }
      }
      if( coincidenciasV == 9 && coincidenciasH == 9 && coincidenciasC == 9){
            return 1;
      } else{
            return 0;
      }
}

function imprime(){
      $('.cell').each(function(){
            $(this).val(sudoku[$(this).attr('id')]);
      });
}

function limpia(){
      $('.cell').each(function(index){
            sudoku[$(this).attr('id')] = 0;
            $(this).val(0);
      });
}

function main(){
      $('.cell').each(function(){
            sudoku[$(this).attr('id')] = $(this).val();
      });
      if(bt(0) == 1){
            imprime();
      }
}
