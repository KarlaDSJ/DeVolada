import { Injectable } from '@angular/core';
import { Observable } from 'rxjs'; // Ayuda a ver el rastro de la peticion
import { HttpClient, HttpHeaders } from '@angular/common/http';

export interface ICarrito {
  idCarrito: Number;
  productos: {
    idProducto: Number
  }[]
}

export interface IProductoCarrito{
  idProducto: number,
  precio: number,
  nombre: string, 
  disponibles: number,
  cantidad: number, 
  imagenes: {
    imagen: string
  }[]
}

export interface IContenerProducto{
  idProducto: number,
  idCarrito: number,
  cantidad: number
}

export interface IMensaje{
  msg: string
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

  obtenerProductos(idCarrito:number) : Observable<IProductoCarrito[]>{
    return this._http.get<IProductoCarrito[]>(`${this._url}/contener?idCarrito=${idCarrito}`)
  }

  cambiarCantidad(idProducto:number, idCarrito:number, cantidad:number): Observable<IContenerProducto>{
    return this._http.put<IContenerProducto>(`${this._url}/contener?idProducto=${idProducto}&idCarrito=${idCarrito}`,{cantidad:cantidad})
  }

  eliminarProducto(idProducto:number, idCarrito:number): Observable<IMensaje>{
    return this._http.delete<IMensaje>(`${this._url}/contener?idProducto=${idProducto}&idCarrito=${idCarrito}`)
  }

  obtenerTotal(idCarrito:number): Observable<number> {
    return this._http.get<number>(`${this._url}/totalCarrito?idCarrito=${idCarrito}`)

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
