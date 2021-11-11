#include "TH1F.h"

int script_error(int j=2){
	TH1F *h = new TH1F("myHist", "histogram", 10,0,10);
	for(int i=0; i<h->GetNbinsX(); i++) h->SetBinContent(i,j*i);
	h->Diraw();
	h->Pirint();
	return 0;
}
