import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';
import { Observable } from 'rxjs';


export interface IDirComprador {
  correo:string, 
  estado:string,
  ciudad:string, 
  colonia:string, 
  cp:number, 
  calle:string, 
  numero:number,
  idDir: number
}

export interface IMsgDir {
  msg: string,
  idDir: number
}

@Injectable({
  providedIn: 'root'
})
export class DireccionCompradorService {

  private _url = "http://127.0.0.1:5000";

  constructor( private _http: HttpClient ) { }

  /**
   * Registra una dirección a un comprador
   * @param correo correo del comprador
   * @param estado estado de la dirección
   * @param ciudad ciudad/alcaldía de la dirección
   * @param colonia colonia de la dirección
   * @param cp código postal de la dirección
   * @param calle calle de la dirección
   * @param numero número exterior de la dirección
   * @returns Mensaje indicando si se pudo registrar o no
   */

  registrarDireccion(correo:string, estado:string, ciudad:string, colonia:string, cp:number, calle:string, numero:number): Observable<IMsgDir>{    
    return  this._http.post<IMsgDir>(`${this._url}/direccionComprador`,{correo: correo, estado:estado, ciudad:ciudad, colonia: colonia, cp: cp, calle: calle, numero:numero})
  }

  /**
   * Obtiene todas las direcciones registradas del comprador 
   * @param correo correo del comprador
   * @returns lista de direcciones registradas del comprador  usando la interfaz IDirComprador
   */

  obtenerDirecciones(correo: string): Observable<IDirComprador[]>{
    return this._http.get<IDirComprador[]>(`${this._url}/direccionComprador/direcciones/${correo}`)
  }

  /**
   * 
   * @param idDir identificador de la dirección que se desea buscar
   * @returns dirección del comprador en formato IDirComprador. 
   *          En caso de que no se pueda obtener se regresa un error con el formato IMensaje
   */
  obtenerDireccion(idDir: number): Observable<IDirComprador>{
    return this._http.get<IDirComprador>(`${this._url}/direccionComprador/${idDir}`)
  }

}
