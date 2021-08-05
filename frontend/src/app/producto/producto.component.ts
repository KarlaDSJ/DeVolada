import { Component, OnInit} from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ProductosService } from "../productos.service";
import { IProducto } from "../productos.service";
import { ResenasService } from '../resenas.service';

@Component({
  selector: 'app-producto',
  templateUrl: './producto.component.html',
  styleUrls: ['./producto.component.css']
})


export class ProductoComponent implements OnInit {

  info: any;
  producto: IProducto;
  id: any = "";
  responsiveOptions:any;

  constructor(private _route:ActivatedRoute, private _productoService: ProductosService, private _ResenasService: ResenasService) {
    //Opciones para hacer responsivo el carrusel de fotos del productos
    this.responsiveOptions = [
      {
          breakpoint: '1024px',
          numVisible: 1,
          numScroll: 1
      }
    ];
  }

  ngOnInit(): void {
    this.id = this._route.snapshot.paramMap.get('id');
    //Nos regresa todos los productos
    this._productoService.getProducto(this.id)
          .subscribe(data => {
            this.producto = data;
            this.info = {'id':this.id, 'nombre':this.producto[0].nombre, 'imagen':this.producto[0].imagenes[0].imagen}
            this._ResenasService.setInfoProducto(this.info)
          })
  }

}
