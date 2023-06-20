import {Component, Inject} from '@angular/core';
import {FormBuilder, FormGroup} from "@angular/forms";
import {DocumentService} from "../document.service";
import {MAT_DIALOG_DATA, MatDialogRef} from "@angular/material/dialog";
import {CoreService} from "../core/core.service";
import {Document} from "../Model/Document";

@Component({
  selector: 'app-document-add-edit',
  templateUrl: './document-add-edit.component.html',
  styleUrls: ['./document-add-edit.component.css']
})
export class DocumentAddEditComponent {
  documentForm: FormGroup;
  errorMessage = "";
  constructor(
    private form_builder: FormBuilder,
    private apiSrv: DocumentService,
    private dialogRef: MatDialogRef<DocumentAddEditComponent>,
    @Inject(MAT_DIALOG_DATA) public data: Document,
    private _coreService: CoreService
  ) {
    this.documentForm = this.form_builder.group({
      author: '',
      title: '',
      pages:'',
      types:'',
      format:'',
    });
  }

  ngOnInit() {
    this.documentForm.patchValue(this.data);
  }

  onFormSubmit(){
    if(this.documentForm.valid){
      if(this.data){
        this.apiSrv.editDocument(this.data.id, this.documentForm.value).subscribe({
          next:(any) =>{
            this._coreService.openSnackBar('Document detail updated!', 'done');
            this.dialogRef.close(true);
          },
          error: (err) =>{
            this.errorMessage = err.error.message;
            this._coreService.openSnackBar(this.errorMessage, 'done');
          }
        })
      }
      else{


        this.apiSrv.createDocument(this.documentForm.value).subscribe({
          next:(any) =>{
            this._coreService.openSnackBar('Document added!', 'done');
            this.dialogRef.close(true);
          },
          error: (err) =>{
            this.errorMessage = err.error.message;
            this._coreService.openSnackBar(this.errorMessage, 'done');
          }
        })
      }
    }
  }
}
