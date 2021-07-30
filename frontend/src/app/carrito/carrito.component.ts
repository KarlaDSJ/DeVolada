import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-carrito',
  templateUrl: './carrito.component.html',
  styleUrls: ['./carrito.component.css']
})
export class CarritoComponent implements OnInit {
  
  nombreP = "Nombre del producto";
  cant = 1;
  idP = 12;
  precioP = 450.00;
  imagenP = "https://i.pinimg.com/originals/1a/ac/af/1aacaff36d04df6b1d189c6f22b4ceb9.jpg";
  disp = 3;

  // Consulta a la base de datos
  listaP = [
    {imagenp: "https://i.pinimg.com/originals/1a/ac/af/1aacaff36d04df6b1d189c6f22b4ceb9.jpg", 
    nombre: "Shiba bb", cant: 1, idP: 12, precioP: 500, disp: 4},
    {imagenp: "https://demascotas.info/wp-content/uploads/2018/01/dog-3098176_1280.jpg", 
    nombre: "Shiba bb", cant: 1, idP: 13, precioP: 800, disp: 1}    
  ];
  

  
  public get total() : number {
    let total = 0;
    this.listaP.forEach(element => {
      total += element.cant*element.precioP;
    });
    return total;
  }
  

  // Aumenta la cantidad de un producto acorde a los disponibles. 
  aumentarCP(indice: number): void{
    if(this.listaP[indice].cant < this.listaP[indice].disp){
      this.listaP[indice].cant++;    
    }
  }

  // Disminuye la cantidad de un producto. El límite es 1
  disminuirCP(indice: number): void{ 
    if (this.listaP[indice].cant >1) {
      this.listaP[indice].cant--;        
    }   
  }


  // Elimina un producto 
  eliminarP(i: number): void{
    this.listaP.splice(i,1);    
  }
  
  constructor() { }

  ngOnInit(): void {
  }

}
