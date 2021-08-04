import { Injectable } from '@angular/core';
import { Observable } from 'rxjs'; // Ayuda a ver el rastro de la peticion
import { HttpClient, HttpHeaders } from '@angular/common/http';

export interface ICarrito {
  idCarrito: Number;
  productos: {
    idProducto: Number
  }[]
}

export interface ICompra{
  'correo':string,
  'idDir': number,
  'tarjeta':string,
  'total':number,
}

export interface IIncluir{
  'idCompra': number,
  'idProducto': number,
  'cantidad':number,
}

@Injectable({
  providedIn: 'root'
})
export class CarritoService {

  private _url = "http://127.0.0.1:5000";
  
  constructor( private _http: HttpClient ) { }

  headers = new HttpHeaders().set('Content-Type', 'application/json');

  crearCarrito(): Observable<ICarrito>{
    return this._http.post<ICarrito>(this._url+"/carrito",{})
  }


  /*
    Registra una compra en la base de datos 
  */
  finalizarCompra(compra:ICompra): Observable<ICompra>{
    const params = JSON.stringify(compra);
    return this._http.post<ICompra>(this._url+"/compra", params, {headers: this.headers});
  }

  /*
    Agrega un producto a la compra en la base de datos
  */
  incluirProductos(incluir:IIncluir): Observable<any>{
    const params = JSON.stringify(incluir);
    return this._http.post<IIncluir>(this._url+"/compra", params, {headers: this.headers});
  }

  /* 
    Nos regresa el Id de los productos comprados y cantidad de los mismos
  */
  productosComprados(idCompra:number): Observable<IIncluir[]>{
    return this._http.get<IIncluir[]>(this._url+"/compra/"+idCompra);
  }
}
