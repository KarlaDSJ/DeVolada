import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CarritoService } from "../carrito.service";
import { ICompra, IIncluir } from "../carrito.service";

@Component({
  selector: 'app-compra-finalizada',
  templateUrl: './compra-finalizada.component.html',
  styleUrls: ['./compra-finalizada.component.css']
})
export class CompraFinalizadaComponent implements OnInit {

  comprador = "Yo merengues";
  correo = "algo@algo.com"
  dir = "Main St 1234, Evolución, Nezahualcóyotl, Ciudad de México, 12345";
  imagenP = "https://i.pinimg.com/originals/1a/ac/af/1aacaff36d04df6b1d189c6f22b4ceb9.jpg";
  nombreP = "Nombre del producto";
  cant = 1;

  listaP = [
    {imagenp: "https://i.pinimg.com/originals/1a/ac/af/1aacaff36d04df6b1d189c6f22b4ceb9.jpg", 
    nombre: "Shiba bb", cant: 1, idP: 12, precioP: 500, disp: 4},
    {imagenp: "https://demascotas.info/wp-content/uploads/2018/01/dog-3098176_1280.jpg", 
    nombre: "Shiba bb", cant: 1, idP: 13, precioP: 800, disp: 1}    
  ];

  idDireccion:string;
  numTarjeta:string;
  idCarrito:string;
  compra:ICompra;
  total: number;

  constructor(private _route:ActivatedRoute, private _carritoService: CarritoService) { }

  ngOnInit(): void {
    //Obtiene el id de la dirección de la compra
    this.idDireccion = this._route.snapshot.paramMap.get('idDir');
    //Obtiene el número de tarjeta de la compra
    this.numTarjeta = this._route.snapshot.paramMap.get('numTar');
    //Obtiene el número de tarjeta de la compra
    this.idCarrito= this._route.snapshot.paramMap.get('idCarrito');
    this.getTotal
  }
  
  getTotal(){
    this._carritoService.obtenerTotal(this.idCarrito)
          .subscribe(data => {
            this.total = data;
            this.compra ={
              'correo': this.correo,
              'idDir': this.idDireccion,
              'tarjeta':this.numTarjeta,
              'total': this.total,
            }
            this.comprar();
          })
  }

  comprar(){
    this._carritoService.finalizarCompra(this.compra)
    .subscribe(data => {
      this.compra = data;
      //this.getProductos();
    })
  }

  getProductos(){
    
  }

}
