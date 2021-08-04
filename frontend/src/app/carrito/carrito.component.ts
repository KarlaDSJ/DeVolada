import { Component, OnInit } from '@angular/core';
import { CarritoService } from '../carrito.service';

@Component({
  selector: 'app-carrito',
  templateUrl: './carrito.component.html',
  styleUrls: ['./carrito.component.css']
})
export class CarritoComponent implements OnInit {
  
  // Consulta a la base de datos 
  idCarrito = 1
  listaP = [];
  
  public get total():number {
    // Ejemplo de cómo se hace con petición a la base
    // this._carritoService.obtenerTotal(this.idCarrito)
    //       .subscribe(data => {
    //         this.total = data
    //       }) 
    let totalP=0
    this.listaP.forEach(element => {
      totalP += element.cant*element.precioP;
    });
    return totalP
  }

  // Aumenta la cantidad de un producto acorde a los disponibles. 
  aumentarCP(indice: number): void{
    if(this.listaP[indice].cant < this.listaP[indice].disp){
      this._carritoService.cambiarCantidad( this.listaP[indice].idP, this.idCarrito, ++this.listaP[indice].cant)
          .subscribe()  
    }
  }

  // Disminuye la cantidad de un producto. El límite es 1
  disminuirCP(indice: number): void{ 
    if (this.listaP[indice].cant >1) {      
      this._carritoService.cambiarCantidad( this.listaP[indice].idP, this.idCarrito, --this.listaP[indice].cant)
          .subscribe()       
    }  
  }

  // Elimina un producto 
  eliminarP(i: number): void{
    this._carritoService.eliminarProducto( this.listaP[i].idP, this.idCarrito)
          .subscribe() 
    // Simulamos que se quita :D 
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
