#include "TH1F.h"

int compiled_script(int j=2){
	TH1F *h = new TH1F("myHist", "histogram", 10,0,10);
	for(int i=0; i<h->GetNbinsX(); i++) h->SetBinContent(i,j*i);
	h->Draw();
	h->Print();
	return 0;
}
