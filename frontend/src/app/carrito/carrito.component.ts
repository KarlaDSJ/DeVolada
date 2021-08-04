import { Component, OnInit } from '@angular/core';
import { IProductoCarrito } from '../carrito.service';
import { CarritoService } from '../carrito.service';

@Component({
  selector: 'app-carrito',
  templateUrl: './carrito.component.html',
  styleUrls: ['./carrito.component.css']
})
export class CarritoComponent implements OnInit {
  
  // Consulta a la base de datos 
  idCarrito = 1

  // Consulta a la base de datos
  listaP = [];  
  
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
  
  constructor(private _carritoService: CarritoService) { }

  ngOnInit(): void {
    this._carritoService.obtenerProductos(this.idCarrito)
          .subscribe(data => {            
            this.listaP = data.map(x => ({
              imagenp:x.imagenes[0].imagen, 
              nombre: x.nombre,
              cant: x.cantidad,
              idP: x.idProducto,
              precioP: x.precio,
              disp: x.disponibles
            }))
          })
  }

}
