import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';
import { Observable } from 'rxjs';

export interface ITarInfo{
  tarjeta: string
}


@Injectable({
  providedIn: 'root'
})
export class MetodoPagoService {

  private _url = "http://127.0.0.1:5000";

  constructor( private _http: HttpClient ) { }

  /**
   * Agrega la tarjeta de un comprador
   * @param correo correo del compradorE
   * @param numero número de tarjeta
   * @param cvv código de seguridad de la tarjeta
   * @param duenio dueño de la tarjeta
   * @param fechaCad fecha de caducidad en formato YYYY-MM-DD
   * @returns Formato con el número de tarjeta y el dueño de la tarjeta 
   */
  agregarTar(correo: string, numero: string, cvv: string, duenio: string, fechaCad) : Observable<any>{
    return this._http.post<any>(`${this._url}/tarjetaComprador`, {correo, numero, cvv, duenio, fechaCad})
  }

  /**
   * Obtiene los números de tarjetas que tiene un comprador 
   * @param correo Correo del comprador
   * @returns Información de las tarjetas que tiene el comprador usando la interfaz ITarInfo en una lista 
   */

  obtenerTarjetas(correo:string): Observable<ITarInfo[]>{
    return this._http.get<ITarInfo[]>(`${this._url}/tarjetasComprador?correo=${correo}`)
  }

  async obtenerTarjeta(correo:string, numero: string): Promise<ITarInfo>{
    return this._http.get<ITarInfo>(`${this._url}/tarjetaComprador?correo=${correo}&numero=${numero}`).toPromise()
  }

}
