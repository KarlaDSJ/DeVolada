import { Component, OnInit } from '@angular/core';
import { ICategoria, ProductosService } from "../../services/productos.service";
import { IProducto } from "../../services/productos.service";
import { Router } from '@angular/router';
import Swal from 'sweetalert2';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-barra-nav-comprador',
  templateUrl: './barra-nav-comprador.component.html',
  styleUrls: ['./barra-nav-comprador.component.css']
})
export class BarraNavCompradorComponent implements OnInit {

  categorias:ICategoria[];
  productos: IProducto[];
  busqueda: boolean = false;


  constructor(private _productoService: ProductosService, private _router:Router, private _cookie: CookieService) { }

  /*
    Carga las categorías en el buscador
  */
  ngOnInit(): void {
    this._productoService.getCaregoria()
          .subscribe(data => {
            this.categorias = data;
          })
  }

  /*
    Hace la petición para buscar productos por nombre y categoría
    Muestra en pantalla los productos 
  */
  buscar(categoria:string, nombre:string){
    if(categoria == "Categorías")
      categoria = "";

    this._productoService.searchProductos(categoria, nombre)
          .subscribe(data => {
            this.productos = data;
            this.busqueda = true;
            if (this.productos.length == 0){
              this.busqueda = false;
              Swal.fire({
                title: 'Lo sentimos :(',
                text: 'No hay productos con esa descripción, inicia sesión como vendedor para registrar uno',
                icon: 'error'
              })
            }
          })
  }

  /*
  Para eliminar de la vista el resultado de la búsqueda
  */
  cerrar(){
    this.productos = [];
    this.busqueda = false;
  }

  logout(){
    while(true){
      
      this._cookie.deleteAll();
      const sigue = this._cookie.check('token_accessC')
      if(!sigue){break;}

    }

    this._router.navigate(['/'])
    
  }
}
