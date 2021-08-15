import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

export interface IadminProducto{
  idProducto: number,
  nombre: String;
  precio: number;
  descripcion: String;
  disponibles: number;
  imagenes: { imagen: String }[];
  categorias: String[];
  
  // Repuesta por parte del sever tras hacer la petición
  error: number,
  mensaje: String
}

export interface ICategoria {
  categoria: String
}

@Injectable({
  providedIn: 'root'
})
export class AdminProductoService {

  private _url = 'http://127.0.0.1:5000/'

  // Id del producto a editar
  id_producto_seleccionado = 0;

  set_Producto_seleccionado(idProducto){
    this.id_producto_seleccionado = idProducto;
    console.log("Se seleccionó el producto <" + this.id_producto_seleccionado + ">");
  }
  
  get_Producto_seleccionado(){
    return this.id_producto_seleccionado;
  }



  constructor( private _http: HttpClient ) {}

  // Realiza la petición al server para dar de alta los datos elementales de un producto 
  daAltaProducto( datosProducto : {correo: string, 
                                   nombre: string, 
                                   precio:number, 
                                   descripcion: string , 
                                   disponibles:number} ): Observable<IadminProducto> {
    return this._http.post<IadminProducto>(this._url+"/producto", datosProducto);
  }

  // Realiza la petición al server para actualizar los datos elementales de un producto BD.
  actualizaProducto( datosProducto : { idProducto: number,
    correo: string, 
    nombre: string, 
    precio:number, 
    descripcion: string , 
    disponibles:number} ): Observable<IadminProducto> {
    let idProducto = datosProducto.idProducto;
    return this._http.patch<IadminProducto>(this._url+"/producto/"+idProducto, datosProducto);
  }

  // Realiza la petición al server para actualizar las categorías de un producto en la BD. 
  actualizaCategorias( idProducto: number, categorias : {categorias : string} )  {
    return this._http.post<IadminProducto>(this._url+`/categoria/actualiza/${idProducto}`, categorias);
  }

  // Realiza la petición al server para actualizar las imágenes del producto en la BD y el sistema.
  actualizaImagenes( idProducto: number, img_files: string[] ):Observable<any> {
    return this._http.patch(this._url + `/imagenes/actualiza/${idProducto}`, img_files)
  }

  // Realiza la petición al server para eliminar un producto de la BD.
  eliminaProducto( idProducto: number )  {
    // Borra el registro del producto de la BD
    return this._http.delete<IadminProducto>(this._url+`/producto/${idProducto}`);
  }

  // Realiza la petición para eliminar las imagenes de la BD y 
  // sus archivos correspondientes del sistema.
  eliminaImagenesProducto( idProducto: number){
    return this._http.delete<any>(this._url+`/imagenes/producto/${idProducto}`)
  }

  // Realiza la petición al server para agregar imágenes a la BD y 
  // guardar sus archivos correspondientes en el sistema.
  subeImagenes( idProducto: number, img_files: string[] ):Observable<any> {
    console.log("hola", {img_files} )
    return this._http.post(this._url + `/imagenes/subir/${idProducto}`, img_files)
  }

  // Realiza la petición al server para agregar imágenes a la BD y 
  // guardar sus archivos correspondientes en el sistema.
  subeImagenesOLD( idProducto: number, img_files: any[] ):Observable<any> {
  
    // Create form data
    const formData = new FormData(); 

    for( let i=0; i< img_files.length; i++ ){
      console.log("00:", img_files[i].file)
      formData.append("imagen["+i+"]", img_files[i].file );
    }
      
    return this._http.post(this._url + `/imagenes/subir/${idProducto}`, formData)
  }

}
