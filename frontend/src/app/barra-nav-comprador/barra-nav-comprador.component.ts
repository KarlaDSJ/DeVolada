import { Component, OnInit } from '@angular/core';
import { ICategoria, ProductosService } from "../productos.service";
import { IProducto } from "../productos.service";

@Component({
  selector: 'app-barra-nav-comprador',
  templateUrl: './barra-nav-comprador.component.html',
  styleUrls: ['./barra-nav-comprador.component.css']
})
export class BarraNavCompradorComponent implements OnInit {

  categorias:ICategoria[];
  productos: IProducto[];
  busqueda: boolean = false;


  constructor(private _productoService: ProductosService) { }

  ngOnInit(): void {
    this._productoService.getCaregoria()
          .subscribe(data => {
            this.categorias = data;
          })
  }

  buscar(categoria:string, nombre:string){
    if(categoria == "Categorías")
      categoria = "";

    this._productoService.searchProductos(categoria, nombre)
          .subscribe(data => {
            console.log(categoria);
            this.productos = data;
            this.busqueda = true;
          })
  }

  cerrar(){
    this.productos = [];
    this.busqueda = false;
  }
}
