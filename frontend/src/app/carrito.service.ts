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

export interface ICarritoComprador{
  idCarrito: number,
  correo: string
}

export interface IMensaje{
  msg: string
}

export interface ICompra{
  idCompra: number,
  correo:string,
  idDir: string,
  tarjeta:string,
  total:number,
}

export interface IIncluir{
  idCompra: number,
  idProducto: number,
  cantidad:number,
}

export interface IDireccion{
  idDie: number,
  correo: string,
  estado: string,
  ciudad: string,
  colonia: string,
  cp: string,
  calle: string,
  numero: string,
}

@Injectable({
  providedIn: 'root'
})
export class CarritoService {

  private _url = "http://127.0.0.1:5000";
  
  constructor( private _http: HttpClient ) { }

  headers = new HttpHeaders().set('Content-Type', 'application/json');

  // PROBAR
  /**
   * Crea un carrito 
   * @returns Interfaz de un carrito 
   */
  async crearCarrito(): Promise<ICarrito>{
    return this._http.post<ICarrito>(this._url+"/carrito",{}).toPromise()
  }

  // PROBAR
  /**
   * Asigna un carrito a un comprador
   * @param idCarrito identificador del carrito
   * @param correo correo del comprador al que se le asignará el carrito  
   * @returns Correo del comprador y id del carrito con la interfaz ICarritoComprador
   */
  async asignarCarrito(idCarrito:number, correo:string): Promise<ICarritoComprador>{
    return this._http.post<ICarritoComprador>(`${this._url}/pertenecer`, {idCarrito, correo}).toPromise()
  }

  /**
   * Agrega un producto a un carrito  
   * @param idProducto identificador del producto a agregar 
   * @param idCarrito identificador del carrito en el que se agregará
   * @returns Mensaje indicando si se puedo o no agregar
   */
  agregarCarrito(idProducto:number, idCarrito:number): Observable<IMensaje>{
    return this._http.post<IMensaje>(`${this._url}/contener`, {idProducto, idCarrito})
  }

  /**
   * Obtiene los productos de un carrito
   * @param idCarrito identificador del carrito
   * @returns Lista de productos que contiene el carrito
   */
  obtenerProductos(idCarrito:number) : Observable<IProductoCarrito[]>{
    return this._http.get<IProductoCarrito[]>(`${this._url}/contener?idCarrito=${idCarrito}`)
  }

  /**
   * Cambia la cantidad de un producto en un carrito. 
   * El producto ya debe de estar en el carrito. 
   * En caso de no poder cambiarla mantiene la cantidad anterior.
   * @param idProducto identificador del producto
   * @param idCarrito identificador del carrito
   * @param cantidad nueva cantidad del producto en el carrito
   * @return Información usando la interfaz IContenerProducto
   */
  cambiarCantidad(idProducto:number, idCarrito:number, cantidad:number): Observable<IContenerProducto>{
    const params={idProducto, idCarrito} 
    return this._http.put<IContenerProducto>(`${this._url}/contener`,{cantidad}, {params})
  }

  /**
   * Elimina un producto de un carrito
   * @param idProducto identificador del producto
   * @param idCarrito identificador del carrito
   * @returns Mensaje indicando si se pudo eliminar o no
   */

  eliminarProducto(idProducto:number, idCarrito:number): Observable<IMensaje>{
    const params={idProducto, idCarrito} 
    return this._http.delete<IMensaje>(`${this._url}/contener`, {params})
  }

  /**
   * Obtiene el total acumulado por los productos y cantidades de un carrito
   * @param idCarrito identificador del carrito
   * @returns Total del carrito
   */
  async obtenerTotal(idCarrito:number): Promise<Observable<number>> {
    return this._http.get<Observable<number>>(`${this._url}/totalCarrito?idCarrito=${idCarrito}`).toPromise()
  }
  
  /**
   * Elimina todos los productos y sus respectivas cantidades de un carrito
   * @param idCarrito identificador del carrito
   * @returns Mensaje indicando si se pudo o no limpiar el carrito
   */
  limpiarCarrito(idCarrito:number): Observable<IMensaje>{
    return this._http.delete<IMensaje>(`${this._url}/limpiarCarrito?idCarrito=${idCarrito}`)
  }

  /*
    Registra una compra en la base de datos 
  */
  async finalizarCompra(correo:string, idDir:number, tarjeta: string, total: number): Promise<ICompra>{
    // const params = JSON.stringify(compra);
    return this._http.post<ICompra>(this._url+"/compra",{correo, idDir, tarjeta, total}).toPromise()
  }
  
  /**
   * Incluye un producto en una compra. Se requiere la cantidad
   * @param producto identificador del producto
   * @param compra identificador de la compra
   * @param cantidad cantidad que se compró
   * @returns Mensaje indicando si se pudo o no agregar usando la interfaz IMensaje
   */
  async incluirProductos(producto:number, compra:number, cantidad: number): Promise<IMensaje>{
    return this._http.post<IMensaje>(`${this._url}/incluir`, {producto, compra, cantidad}).toPromise()
  }

  
}
