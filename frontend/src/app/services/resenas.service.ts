import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders  } from '@angular/common/http';
import {HttpParams} from "@angular/common/http";
import { Observable } from 'rxjs';
import { ProductosService } from './productos.service';

/**
 * Interface para declarar los datos que vamos a ocupar en la reseña
 */
export interface IResena {
  idProducto: String;
  correo: String;
  calificacion: number;
  opinion: String;
  nombre: String;
  promedio: number;
  total: number;
  msg: string;
}

/**
 * Interface para declarar los datos que vamos a ocupar de un producto
 */
export interface IInfoProducto {
  idProducto: string;
  nombre: String;
  imagen: String;
}

@Injectable({
  providedIn: 'root'
})

/**
 * La clase del servicio de Resenas
 */
export class ResenasService {
  private _url = "http://127.0.0.1:5000";//la url del servidor para mandar las peticiones

  infoProducto: IInfoProducto;
  headers = new HttpHeaders().set('Content-Type', 'application/json');

  /**
   * Constructor de la clase
   * @param _http el cliente para generar las peticiones por json 
   */

  constructor(private _http: HttpClient) { }


  /**
   * Metodo para modificar los datos de un producto
   * @param info los datos del producto
   */ 

  setInfoProducto(info: IInfoProducto){
    this.infoProducto = info;
  }


  /**
   * Metodo para mostrar los datos de un producto
   * @param info los datos del producto
   */ 

  getInfoProducto(): IInfoProducto{
    return this.infoProducto;
  }


  /**
   * Metodo para crear una reseña
   * @param idProducto el id del Producto que deseamos
   * @param correo el correo del usuario que hace la reseña
   * @param calificacion la calificación que asigna el usuario
   * @param opinion la opinión del usuario 
   * @returns un JSON con los datos anteriores
   */

  crearResenas(idProducto:string, correo:string, calificacion:number, opinion:string) : Observable<IResena[]>{
    
    const params = JSON.stringify({
      'idProducto': idProducto,
      'correo': correo,
      'calificacion': calificacion,
      'opinion': opinion
    });
    
    return this._http.post<IResena[]>(this._url+"/crearResena",  params, {headers: this.headers})
  }


  /**
   * Metodo que muestra todas las reseñas de un producto
   * @param idProducto el id del Producto que deseamos 
   * @returns lista de resenas registradas usando la interfaz IResena
   */
  mostrarResenas(idProducto:string): Observable<IResena[]>{
    return this._http.get<IResena[]>(this._url+"/mostrarResenas/"+idProducto)
  }


  /**
   * Metodo que muestra las primeras 5 reseñas de un producto
   * @param idProducto el id del Producto que deseamos 
   * @returns lista de resenas registradas usando la interfaz IResena
   */

  mostrar5Resenas(idProducto:string): Observable<IResena[]>{
    return this._http.get<IResena[]>(this._url+"/resenas/"+idProducto)
  }


  /**
   * Metodo que muestra el promedio del # total de calificaciones de 
   * de un producto
   * @param idProducto el id del Producto que deseamos 
   * @returns el promedio usando la interfaz IResena
   */

  obtenerPromedio(idProducto:string): Observable<IResena>{
    return this._http.get<IResena>(this._url+"/promedio/"+idProducto)
  }


  /**
   * Metodo que muestra el # total reseñas de un producto
   * @param idProducto el id del Producto que deseamos 
   * @returns el total usando la interfaz IResena
   */

  obtenerTotal(idProducto:string): Observable<IResena>{
    return this._http.get<IResena>(this._url+"/totalResenas/"+idProducto)
  }


  /**
   * Metodo que verifica que un usuario haya comprado un producto para
   * poder dejar una reseña en él
   * @param idProducto el id del Producto que deseamos
   */

   verificar(idProducto:string): Observable<IResena>{
    return this._http.get<IResena>(this._url+"/verificar/"+idProducto)
  }
}
