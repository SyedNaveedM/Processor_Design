import fileinput
import pandas as pd
import tabulate

IM1=[]
DM1=[]
for line in fileinput.input(files='machineCode.txt'):
    IM1.append(line[:-1])
pc=0
#we are implementing the memory using maps
DM={8000:0,8001:0,8002:0,8003:0,8004:0,8005:0,8006:0,8007:0,8008:0,8009:0,8010:0,8011:0,8012:0,8013:0,8014:0,8015:0,8016:0,8017:0,8018:0,8019:0,8020:0,8021:0,8022:0,8023:0,8024:0,8025:0,8026:0,8027:0,8028:0,8029:0,8030:0,8031:0,8032:0,8033:0,8034:0,8035:0,8036:0,8037:0,8038:0,8039:0,8040:0,8041:0,8042:0,8043:0,8044:0,8045:0,8046:0,8047:0,8048:0,8049:0,8050:0,8051:0,8052:0,8053:0,8054:0,8055:0,8056:0,8057:0,8058:0,8059:0,8060:0,8061:0,8062:0,8063:0,8064:0,8065:0,8066:0,8067:0,8068:0,8069:0,8070:0,8071:0,8072:0,8073:0,8074:0,8075:0,8076:0,8077:0,8078:0,8079:0,8080:0,8081:0,8082:0,8083:0,8084:0,8085:0,8086:0,8087:0,8088:0,8089:0,8090:0,8091:0,8092:0,8093:0,8094:0,8095:0,8096:0,8097:0,8098:0,8099:0,8100:0,8101:0,8102:0,8103:0,8104:0,8105:0,8106:0,8107:0,8108:0,8109:0,8110:0,8111:0,8112:0,8113:0,8114:0,8115:0,8116:0,8117:0,8118:0,8119:0,8120:0,8121:0,8122:0,8123:0,8124:0,8125:0,8126:0,8127:0,8128:0,8129:0,8130:0,8131:0,8132:0,8133:0,8134:0,8135:0,8136:0,8137:0,8138:0,8139:0,8140:0,8141:0,8142:0,8143:0,8144:0,8145:0,8146:0,8147:0,8148:0,8149:0,8150:0,8151:0,8152:0,8153:0,8154:0,8155:0,8156:0,8157:0,8158:0,8159:0,8160:0,8161:0,8162:0,8163:0,8164:0,8165:0,8166:0,8167:0,8168:0,8169:0,8170:0,8171:0,8172:0,8173:0,8174:0,8175:0,8176:0,8177:0,8178:0,8179:0,8180:0,8181:0,8182:0,8183:0,8184:0,8185:0,8186:0,8187:0,8188:0,8189:0,8190:0,8191:0,8192:0,8193:0,8194:0,8195:0,8196:0,8197:0,8198:0,8199:0,8200:0,8201:0,8202:0,8203:0,8204:0,8205:0,8206:0,8207:0,8208:0,8209:0,8210:0,8211:0,8212:0,8213:0,8214:0,8215:0,8216:0,8217:0,8218:0,8219:0,8220:0,8221:0,8222:0,8223:0,8224:0,8225:0,8226:0,8227:0,8228:0,8229:0,8230:0,8231:0,8232:0,8233:0,8234:0,8235:0,8236:0,8237:0,8238:0,8239:0,8240:0,8241:0,8242:0,8243:0,8244:0,8245:0,8246:0,8247:0,8248:0,8249:0,8250:0,8251:0,8252:0,8253:0,8254:0,8255:0,8256:0,8257:0,8258:0,8259:0,8260:0,8261:0,8262:0,8263:0,8264:0,8265:0,8266:0,8267:0,8268:0,8269:0,8270:0,8271:0,8272:0,8273:0,8274:0,8275:0,8276:0,8277:0,8278:0,8279:0,8280:0,8281:0,8282:0,8283:0,8284:0,8285:0,8286:0,8287:0,8288:0,8289:0,8290:0,8291:0,8292:0,8293:0,8294:0,8295:0,8296:0,8297:0,8298:0,8299:0,8300:0,8301:0,8302:0,8303:0,8304:0,8305:0,8306:0,8307:0,8308:0,8309:0,8310:0,8311:0,8312:0,8313:0,8314:0,8315:0,8316:0,8317:0,8318:0,8319:0,8320:0,8321:0,8322:0,8323:0,8324:0,8325:0,8326:0,8327:0,8328:0,8329:0,8330:0,8331:0,8332:0,8333:0,8334:0,8335:0,8336:0,8337:0,8338:0,8339:0,8340:0,8341:0,8342:0,8343:0,8344:0,8345:0,8346:0,8347:0,8348:0,8349:0,8350:0,8351:0,8352:0,8353:0,8354:0,8355:0,8356:0,8357:0,8358:0,8359:0,8360:0,8361:0,8362:0,8363:0,8364:0,8365:0,8366:0,8367:0,8368:0,8369:0,8370:0,8371:0,8372:0,8373:0,8374:0,8375:0,8376:0,8377:0,8378:0,8379:0,8380:0,8381:0,8382:0,8383:0,8384:0,8385:0,8386:0,8387:0,8388:0,8389:0,8390:0,8391:0,8392:0,8393:0,8394:0,8395:0,8396:0,8397:0,8398:0,8399:0,8400:0,8401:0,8402:0,8403:0,8404:0,8405:0,8406:0,8407:0,8408:0,8409:0,8410:0,8411:0,8412:0,8413:0,8414:0,8415:0,8416:0,8417:0,8418:0,8419:0,8420:0,8421:0,8422:0,8423:0,8424:0,8425:0,8426:0,8427:0,8428:0,8429:0,8430:0,8431:0,8432:0,8433:0,8434:0,8435:0,8436:0,8437:0,8438:0,8439:0,8440:0,8441:0,8442:0,8443:0,8444:0,8445:0,8446:0,8447:0,8448:0,8449:0,8450:0,8451:0,8452:0,8453:0,8454:0,8455:0,8456:0,8457:0,8458:0,8459:0,8460:0,8461:0,8462:0,8463:0,8464:0,8465:0,8466:0,8467:0,8468:0,8469:0,8470:0,8471:0,8472:0,8473:0,8474:0,8475:0,8476:0,8477:0,8478:0,8479:0,8480:0,8481:0,8482:0,8483:0,8484:0,8485:0,8486:0,8487:0,8488:0,8489:0,8490:0,8491:0,8492:0,8493:0,8494:0,8495:0,8496:0,8497:0,8498:0,8499:0,8500:0,8501:0,8502:0,8503:0,8504:0,8505:0,8506:0,8507:0,8508:0,8509:0,8510:0,8511:0,8512:0,8513:0,8514:0,8515:0,8516:0,8517:0,8518:0,8519:0,8520:0,8521:0,8522:0,8523:0,8524:0,8525:0,8526:0,8527:0,8528:0,8529:0,8530:0,8531:0,8532:0,8533:0,8534:0,8535:0,8536:0,8537:0,8538:0,8539:0,8540:0,8541:0,8542:0,8543:0,8544:0,8545:0,8546:0,8547:0,8548:0,8549:0,8550:0,8551:0,8552:0,8553:0,8554:0,8555:0,8556:0,8557:0,8558:0,8559:0,8560:0,8561:0,8562:0,8563:0,8564:0,8565:0,8566:0,8567:0,8568:0,8569:0,8570:0,8571:0,8572:0,8573:0,8574:0,8575:0,8576:0,8577:0,8578:0,8579:0,8580:0,8581:0,8582:0,8583:0,8584:0,8585:0,8586:0,8587:0,8588:0,8589:0,8590:0,8591:0,8592:0,8593:0,8594:0,8595:0,8596:0,8597:0,8598:0,8599:0,8600:0,8601:0,8602:0,8603:0,8604:0,8605:0,8606:0,8607:0,8608:0,8609:0,8610:0,8611:0,8612:0,8613:0,8614:0,8615:0,8616:0,8617:0,8618:0,8619:0,8620:0,8621:0,8622:0,8623:0,8624:0,8625:0,8626:0,8627:0,8628:0,8629:0,8630:0,8631:0,8632:0,8633:0,8634:0,8635:0,8636:0,8637:0,8638:0,8639:0,8640:0,8641:0,8642:0,8643:0,8644:0,8645:0,8646:0,8647:0,8648:0,8649:0,8650:0,8651:0,8652:0,8653:0,8654:0,8655:0,8656:0,8657:0,8658:0,8659:0,8660:0,8661:0,8662:0,8663:0,8664:0,8665:0,8666:0,8667:0,8668:0,8669:0,8670:0,8671:0,8672:0,8673:0,8674:0,8675:0,8676:0,8677:0,8678:0,8679:0,8680:0,8681:0,8682:0,8683:0,8684:0,8685:0,8686:0,8687:0,8688:0,8689:0,8690:0,8691:0,8692:0,8693:0,8694:0,8695:0,8696:0,8697:0,8698:0,8699:0,8700:0,8701:0,8702:0,8703:0,8704:0,8705:0,8706:0,8707:0,8708:0,8709:0,8710:0,8711:0,8712:0,8713:0,8714:0,8715:0,8716:0,8717:0,8718:0,8719:0,8720:0,8721:0,8722:0,8723:0,8724:0,8725:0,8726:0,8727:0,8728:0,8729:0,8730:0,8731:0,8732:0,8733:0,8734:0,8735:0,8736:0,8737:0,8738:0,8739:0,8740:0,8741:0,8742:0,8743:0,8744:0,8745:0,8746:0,8747:0,8748:0,8749:0,8750:0,8751:0,8752:0,8753:0,8754:0,8755:0,8756:0,8757:0,8758:0,8759:0,8760:0,8761:0,8762:0,8763:0,8764:0,8765:0,8766:0,8767:0,8768:0,8769:0,8770:0,8771:0,8772:0,8773:0,8774:0,8775:0,8776:0,8777:0,8778:0,8779:0,8780:0,8781:0,8782:0,8783:0,8784:0,8785:0,8786:0,8787:0,8788:0,8789:0,8790:0,8791:0,8792:0,8793:0,8794:0,8795:0,8796:0,8797:0,8798:0,8799:0,8800:0,8801:0,8802:0,8803:0,8804:0,8805:0,8806:0,8807:0,8808:0,8809:0,8810:0,8811:0,8812:0,8813:0,8814:0,8815:0,8816:0,8817:0,8818:0,8819:0,8820:0,8821:0,8822:0,8823:0,8824:0,8825:0,8826:0,8827:0,8828:0,8829:0,8830:0,8831:0,8832:0,8833:0,8834:0,8835:0,8836:0,8837:0,8838:0,8839:0,8840:0,8841:0,8842:0,8843:0,8844:0,8845:0,8846:0,8847:0,8848:0,8849:0,8850:0,8851:0,8852:0,8853:0,8854:0,8855:0,8856:0,8857:0,8858:0,8859:0,8860:0,8861:0,8862:0,8863:0,8864:0,8865:0,8866:0,8867:0,8868:0,8869:0,8870:0,8871:0,8872:0,8873:0,8874:0,8875:0,8876:0,8877:0,8878:0,8879:0,8880:0,8881:0,8882:0,8883:0,8884:0,8885:0,8886:0,8887:0,8888:0,8889:0,8890:0,8891:0,8892:0,8893:0,8894:0,8895:0,8896:0,8897:0,8898:0,8899:0,8900:0,8901:0,8902:0,8903:0,8904:0,8905:0,8906:0,8907:0,8908:0,8909:0,8910:0,8911:0,8912:0,8913:0,8914:0,8915:0,8916:0,8917:0,8918:0,8919:0,8920:0,8921:0,8922:0,8923:0,8924:0,8925:0,8926:0,8927:0,8928:0,8929:0,8930:0,8931:0,8932:0,8933:0,8934:0,8935:0,8936:0,8937:0,8938:0,8939:0,8940:0,8941:0,8942:0,8943:0,8944:0,8945:0,8946:0,8947:0,8948:0,8949:0,8950:0,8951:0,8952:0,8953:0,8954:0,8955:0,8956:0,8957:0,8958:0,8959:0,8960:0,8961:0,8962:0,8963:0,8964:0,8965:0,8966:0,8967:0,8968:0,8969:0,8970:0,8971:0,8972:0,8973:0,8974:0,8975:0,8976:0,8977:0,8978:0,8979:0,8980:0,8981:0,8982:0,8983:0,8984:0,8985:0,8986:0,8987:0,8988:0,8989:0,8990:0,8991:0,8992:0,8993:0,8994:0,8995:0,8996:0,8997:0,8998:0,8999:0,9000:0,9001:0,9002:0,9003:0,9004:0,9005:0,9006:0,9007:0,9008:0,9009:0,9010:0,9011:0,9012:0,9013:0,9014:0,9015:0,9016:0,9017:0,9018:0,9019:0,9020:0,9021:0,9022:0,9023:0,9024:0,9025:0,9026:0,9027:0,9028:0,9029:0,9030:0,9031:0,9032:0,9033:0,9034:0,9035:0,9036:0,9037:0,9038:0,9039:0,9040:0,9041:0,9042:0,9043:0,9044:0,9045:0,9046:0,9047:0,9048:0,9049:0,9050:0,9051:0,9052:0,9053:0,9054:0,9055:0,9056:0,9057:0,9058:0,9059:0,9060:0,9061:0,9062:0,9063:0,9064:0,9065:0,9066:0,9067:0,9068:0,9069:0,9070:0,9071:0,9072:0,9073:0,9074:0,9075:0,9076:0,9077:0,9078:0,9079:0,9080:0,9081:0,9082:0,9083:0,9084:0,9085:0,9086:0,9087:0,9088:0,9089:0,9090:0,9091:0,9092:0,9093:0,9094:0,9095:0,9096:0,9097:0,9098:0,9099:0,9100:0,9101:0,9102:0,9103:0,9104:0,9105:0,9106:0,9107:0,9108:0,9109:0,9110:0,9111:0,9112:0,9113:0,9114:0,9115:0,9116:0,9117:0,9118:0,9119:0,9120:0,9121:0,9122:0,9123:0,9124:0,9125:0,9126:0,9127:0,9128:0,9129:0,9130:0,9131:0,9132:0,9133:0,9134:0,9135:0,9136:0,9137:0,9138:0,9139:0,9140:0,9141:0,9142:0,9143:0,9144:0,9145:0,9146:0,9147:0,9148:0,9149:0,9150:0,9151:0,9152:0,9153:0,9154:0,9155:0,9156:0,9157:0,9158:0,9159:0,9160:0,9161:0,9162:0,9163:0,9164:0,9165:0,9166:0,9167:0,9168:0,9169:0,9170:0,9171:0,9172:0,9173:0,9174:0,9175:0,9176:0,9177:0,9178:0,9179:0,9180:0,9181:0,9182:0,9183:0,9184:0,9185:0,9186:0,9187:0,9188:0,9189:0,9190:0,9191:0,9192:0,9193:0,9194:0,9195:0,9196:0,9197:0,9198:0,9199:0,9200:0,9201:0,9202:0,9203:0,9204:0,9205:0,9206:0,9207:0,9208:0,9209:0,9210:0,9211:0,9212:0,9213:0,9214:0,9215:0,9216:0,9217:0,9218:0,9219:0,9220:0,9221:0,9222:0,9223:0,9224:0,9225:0,9226:0,9227:0,9228:0,9229:0,9230:0,9231:0,9232:0,9233:0,9234:0,9235:0,9236:0,9237:0,9238:0,9239:0,9240:0,9241:0,9242:0,9243:0,9244:0,9245:0,9246:0,9247:0,9248:0,9249:0,9250:0,9251:0,9252:0,9253:0,9254:0,9255:0,9256:0,9257:0,9258:0,9259:0,9260:0,9261:0,9262:0,9263:0,9264:0,9265:0,9266:0,9267:0,9268:0,9269:0,9270:0,9271:0,9272:0,9273:0,9274:0,9275:0,9276:0,9277:0,9278:0,9279:0,9280:0,9281:0,9282:0,9283:0,9284:0,9285:0,9286:0,9287:0,9288:0,9289:0,9290:0,9291:0,9292:0,9293:0,9294:0,9295:0,9296:0,9297:0,9298:0,9299:0,9300:0,9301:0,9302:0,9303:0,9304:0,9305:0,9306:0,9307:0,9308:0,9309:0,9310:0,9311:0,9312:0,9313:0,9314:0,9315:0,9316:0,9317:0,9318:0,9319:0,9320:0,9321:0,9322:0,9323:0,9324:0,9325:0,9326:0,9327:0,9328:0,9329:0,9330:0,9331:0,9332:0,9333:0,9334:0,9335:0,9336:0,9337:0,9338:0,9339:0,9340:0,9341:0,9342:0,9343:0,9344:0,9345:0,9346:0,9347:0,9348:0,9349:0,9350:0,9351:0,9352:0,9353:0,9354:0,9355:0,9356:0,9357:0,9358:0,9359:0,9360:0,9361:0,9362:0,9363:0,9364:0,9365:0,9366:0,9367:0,9368:0,9369:0,9370:0,9371:0,9372:0,9373:0,9374:0,9375:0,9376:0,9377:0,9378:0,9379:0,9380:0,9381:0,9382:0,9383:0,9384:0,9385:0,9386:0,9387:0,9388:0,9389:0,9390:0,9391:0,9392:0,9393:0,9394:0,9395:0,9396:0,9397:0,9398:0,9399:0,9400:0,9401:0,9402:0,9403:0,9404:0,9405:0,9406:0,9407:0,9408:0,9409:0,9410:0,9411:0,9412:0,9413:0,9414:0,9415:0,9416:0,9417:0,9418:0,9419:0,9420:0,9421:0,9422:0,9423:0,9424:0,9425:0,9426:0,9427:0,9428:0,9429:0,9430:0,9431:0,9432:0,9433:0,9434:0,9435:0,9436:0,9437:0,9438:0,9439:0,9440:0,9441:0,9442:0,9443:0,9444:0,9445:0,9446:0,9447:0,9448:0,9449:0,9450:0,9451:0,9452:0,9453:0,9454:0,9455:0,9456:0,9457:0,9458:0,9459:0,9460:0,9461:0,9462:0,9463:0,9464:0,9465:0,9466:0,9467:0,9468:0,9469:0,9470:0,9471:0,9472:0,9473:0,9474:0,9475:0,9476:0,9477:0,9478:0,9479:0,9480:0,9481:0,9482:0,9483:0,9484:0,9485:0,9486:0,9487:0,9488:0,9489:0,9490:0,9491:0,9492:0,9493:0,9494:0,9495:0,9496:0,9497:0,9498:0,9499:0,9500:0,9501:0,9502:0,9503:0,9504:0,9505:0,9506:0,9507:0,9508:0,9509:0,9510:0,9511:0,9512:0,9513:0,9514:0,9515:0,9516:0,9517:0,9518:0,9519:0,9520:0,9521:0,9522:0,9523:0,9524:0,9525:0,9526:0,9527:0,9528:0,9529:0,9530:0,9531:0,9532:0,9533:0,9534:0,9535:0,9536:0,9537:0,9538:0,9539:0,9540:0,9541:0,9542:0,9543:0,9544:0,9545:0,9546:0,9547:0,9548:0,9549:0,9550:0,9551:0,9552:0,9553:0,9554:0,9555:0,9556:0,9557:0,9558:0,9559:0,9560:0,9561:0,9562:0,9563:0,9564:0,9565:0,9566:0,9567:0,9568:0,9569:0,9570:0,9571:0,9572:0,9573:0,9574:0,9575:0,9576:0,9577:0,9578:0,9579:0,9580:0,9581:0,9582:0,9583:0,9584:0,9585:0,9586:0,9587:0,9588:0,9589:0,9590:0,9591:0,9592:0,9593:0,9594:0,9595:0,9596:0,9597:0,9598:0,9599:0,9600:0,9601:0,9602:0,9603:0,9604:0,9605:0,9606:0,9607:0,9608:0,9609:0,9610:0,9611:0,9612:0,9613:0,9614:0,9615:0,9616:0,9617:0,9618:0,9619:0,9620:0,9621:0,9622:0,9623:0,9624:0,9625:0,9626:0,9627:0,9628:0,9629:0,9630:0,9631:0,9632:0,9633:0,9634:0,9635:0,9636:0,9637:0,9638:0,9639:0,9640:0,9641:0,9642:0,9643:0,9644:0,9645:0,9646:0,9647:0,9648:0,9649:0,9650:0,9651:0,9652:0,9653:0,9654:0,9655:0,9656:0,9657:0,9658:0,9659:0,9660:0,9661:0,9662:0,9663:0,9664:0,9665:0,9666:0,9667:0,9668:0,9669:0,9670:0,9671:0,9672:0,9673:0,9674:0,9675:0,9676:0,9677:0,9678:0,9679:0,9680:0,9681:0,9682:0,9683:0,9684:0,9685:0,9686:0,9687:0,9688:0,9689:0,9690:0,9691:0,9692:0,9693:0,9694:0,9695:0,9696:0,9697:0,9698:0,9699:0,9700:0,9701:0,9702:0,9703:0,9704:0,9705:0,9706:0,9707:0,9708:0,9709:0,9710:0,9711:0,9712:0,9713:0,9714:0,9715:0,9716:0,9717:0,9718:0,9719:0,9720:0,9721:0,9722:0,9723:0,9724:0,9725:0,9726:0,9727:0,9728:0,9729:0,9730:0,9731:0,9732:0,9733:0,9734:0,9735:0,9736:0,9737:0,9738:0,9739:0,9740:0,9741:0,9742:0,9743:0,9744:0,9745:0,9746:0,9747:0,9748:0,9749:0,9750:0,9751:0,9752:0,9753:0,9754:0,9755:0,9756:0,9757:0,9758:0,9759:0,9760:0,9761:0,9762:0,9763:0,9764:0,9765:0,9766:0,9767:0,9768:0,9769:0,9770:0,9771:0,9772:0,9773:0,9774:0,9775:0,9776:0,9777:0,9778:0,9779:0,9780:0,9781:0,9782:0,9783:0,9784:0,9785:0,9786:0,9787:0,9788:0,9789:0,9790:0,9791:0,9792:0,9793:0,9794:0,9795:0,9796:0,9797:0,9798:0,9799:0,9800:0,9801:0,9802:0,9803:0,9804:0,9805:0,9806:0,9807:0,9808:0,9809:0,9810:0,9811:0,9812:0,9813:0,9814:0,9815:0,9816:0,9817:0,9818:0,9819:0,9820:0,9821:0,9822:0,9823:0,9824:0,9825:0,9826:0,9827:0,9828:0,9829:0,9830:0,9831:0,9832:0,9833:0,9834:0,9835:0,9836:0,9837:0,9838:0,9839:0,9840:0,9841:0,9842:0,9843:0,9844:0,9845:0,9846:0,9847:0,9848:0,9849:0,9850:0,9851:0,9852:0,9853:0,9854:0,9855:0,9856:0,9857:0,9858:0,9859:0,9860:0,9861:0,9862:0,9863:0,9864:0,9865:0,9866:0,9867:0,9868:0,9869:0,9870:0,9871:0,9872:0,9873:0,9874:0,9875:0,9876:0,9877:0,9878:0,9879:0,9880:0,9881:0,9882:0,9883:0,9884:0,9885:0,9886:0,9887:0,9888:0,9889:0,9890:0,9891:0,9892:0,9893:0,9894:0,9895:0,9896:0,9897:0,9898:0,9899:0,9900:0,9901:0,9902:0,9903:0,9904:0,9905:0,9906:0,9907:0,9908:0,9909:0,9910:0,9911:0,9912:0,9913:0,9914:0,9915:0,9916:0,9917:0,9918:0,9919:0,9920:0,9921:0,9922:0,9923:0,9924:0,9925:0,9926:0,9927:0,9928:0,9929:0,9930:0,9931:0,9932:0,9933:0,9934:0,9935:0,9936:0,9937:0,9938:0,9939:0,9940:0,9941:0,9942:0,9943:0,9944:0,9945:0,9946:0,9947:0,9948:0,9949:0,9950:0,9951:0,9952:0,9953:0,9954:0,9955:0,9956:0,9957:0,9958:0,9959:0,9960:0,9961:0,9962:0,9963:0,9964:0,9965:0,9966:0,9967:0,9968:0,9969:0,9970:0,9971:0,9972:0,9973:0,9974:0,9975:0,9976:0,9977:0,9978:0,9979:0,9980:0,9981:0,9982:0,9983:0,9984:0,9985:0,9986:0,9987:0,9988:0,9989:0,9990:0,9991:0,9992:0,9993:0,9994:0,9995:0,9996:0,9997:0,9998:0,9999:0,10000:0}
IM={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0,24:0,25:0,26:0,27:0,28:0,29:0,30:0,31:0,32:0,33:0,34:0,35:0,36:0,37:0,38:0,39:0,40:0,41:0,42:0,43:0,44:0,45:0,46:0,47:0,48:0,49:0,50:0,51:0,52:0,53:0,54:0,55:0,56:0,57:0,58:0,59:0,60:0,61:0,62:0,63:0,64:0,65:0,66:0,67:0,68:0,69:0,70:0,71:0,72:0,73:0,74:0,75:0,76:0,77:0,78:0,79:0,80:0,81:0,82:0,83:0,84:0,85:0,86:0,87:0,88:0,89:0,90:0,91:0,92:0,93:0,94:0,95:0,96:0,97:0,98:0,99:0,100:0,101:0,102:0,103:0,104:0,105:0,106:0,107:0,108:0,109:0,110:0,111:0,112:0,113:0,114:0,115:0,116:0,117:0,118:0,119:0,120:0,121:0,122:0,123:0,124:0,125:0,126:0,127:0,128:0,129:0,130:0,131:0,132:0,133:0,134:0,135:0,136:0,137:0,138:0,139:0,140:0,141:0,142:0,143:0,144:0,145:0,146:0,147:0,148:0,149:0,150:0,151:0,152:0,153:0,154:0,155:0,156:0,157:0,158:0,159:0,160:0,161:0,162:0,163:0,164:0,165:0,166:0,167:0,168:0,169:0,170:0,171:0,172:0,173:0,174:0,175:0,176:0,177:0,178:0,179:0,180:0,181:0,182:0,183:0,184:0,185:0,186:0,187:0,188:0,189:0,190:0,191:0,192:0,193:0,194:0,195:0,196:0,197:0,198:0,199:0,200:0,201:0,202:0,203:0,204:0,205:0,206:0,207:0,208:0,209:0,210:0,211:0,212:0,213:0,214:0,215:0,216:0,217:0,218:0,219:0,220:0,221:0,222:0,223:0,224:0,225:0,226:0,227:0,228:0,229:0,230:0,231:0,232:0,233:0,234:0,235:0,236:0,237:0,238:0,239:0,240:0,241:0,242:0,243:0,244:0,245:0,246:0,247:0,248:0,249:0,250:0,251:0,252:0,253:0,254:0,255:0,256:0,257:0,258:0,259:0,260:0,261:0,262:0,263:0,264:0,265:0,266:0,267:0,268:0,269:0,270:0,271:0,272:0,273:0,274:0,275:0,276:0,277:0,278:0,279:0,280:0,281:0,282:0,283:0,284:0,285:0,286:0,287:0,288:0,289:0,290:0,291:0,292:0,293:0,294:0,295:0,296:0,297:0,298:0,299:0,300:0,301:0,302:0,303:0,304:0,305:0,306:0,307:0,308:0,309:0,310:0,311:0,312:0,313:0,314:0,315:0,316:0,317:0,318:0,319:0,320:0,321:0,322:0,323:0,324:0,325:0,326:0,327:0,328:0,329:0,330:0,331:0,332:0,333:0,334:0,335:0,336:0,337:0,338:0,339:0,340:0,341:0,342:0,343:0,344:0,345:0,346:0,347:0,348:0,349:0,350:0,351:0,352:0,353:0,354:0,355:0,356:0,357:0,358:0,359:0,360:0,361:0,362:0,363:0,364:0,365:0,366:0,367:0,368:0,369:0,370:0,371:0,372:0,373:0,374:0,375:0,376:0,377:0,378:0,379:0,380:0,381:0,382:0,383:0,384:0,385:0,386:0,387:0,388:0,389:0,390:0,391:0,392:0,393:0,394:0,395:0,396:0,397:0,398:0,399:0,400:0,401:0,402:0,403:0,404:0,405:0,406:0,407:0,408:0,409:0,410:0,411:0,412:0,413:0,414:0,415:0,416:0,417:0,418:0,419:0,420:0,421:0,422:0,423:0,424:0,425:0,426:0,427:0,428:0,429:0,430:0,431:0,432:0,433:0,434:0,435:0,436:0,437:0,438:0,439:0,440:0,441:0,442:0,443:0,444:0,445:0,446:0,447:0,448:0,449:0,450:0,451:0,452:0,453:0,454:0,455:0,456:0,457:0,458:0,459:0,460:0,461:0,462:0,463:0,464:0,465:0,466:0,467:0,468:0,469:0,470:0,471:0,472:0,473:0,474:0,475:0,476:0,477:0,478:0,479:0,480:0,481:0,482:0,483:0,484:0,485:0,486:0,487:0,488:0,489:0,490:0,491:0,492:0,493:0,494:0,495:0,496:0,497:0,498:0,499:0,500:0,501:0,502:0,503:0,504:0,505:0,506:0,507:0,508:0,509:0,510:0,511:0,512:0,513:0,514:0,515:0,516:0,517:0,518:0,519:0,520:0,521:0,522:0,523:0,524:0,525:0,526:0,527:0,528:0,529:0,530:0,531:0,532:0,533:0,534:0,535:0,536:0,537:0,538:0,539:0,540:0,541:0,542:0,543:0,544:0,545:0,546:0,547:0,548:0,549:0,550:0,551:0,552:0,553:0,554:0,555:0,556:0,557:0,558:0,559:0,560:0,561:0,562:0,563:0,564:0,565:0,566:0,567:0,568:0,569:0,570:0,571:0,572:0,573:0,574:0,575:0,576:0,577:0,578:0,579:0,580:0,581:0,582:0,583:0,584:0,585:0,586:0,587:0,588:0,589:0,590:0,591:0,592:0,593:0,594:0,595:0,596:0,597:0,598:0,599:0,600:0,601:0,602:0,603:0,604:0,605:0,606:0,607:0,608:0,609:0,610:0,611:0,612:0,613:0,614:0,615:0,616:0,617:0,618:0,619:0,620:0,621:0,622:0,623:0,624:0,625:0,626:0,627:0,628:0,629:0,630:0,631:0,632:0,633:0,634:0,635:0,636:0,637:0,638:0,639:0,640:0,641:0,642:0,643:0,644:0,645:0,646:0,647:0,648:0,649:0,650:0,651:0,652:0,653:0,654:0,655:0,656:0,657:0,658:0,659:0,660:0,661:0,662:0,663:0,664:0,665:0,666:0,667:0,668:0,669:0,670:0,671:0,672:0,673:0,674:0,675:0,676:0,677:0,678:0,679:0,680:0,681:0,682:0,683:0,684:0,685:0,686:0,687:0,688:0,689:0,690:0,691:0,692:0,693:0,694:0,695:0,696:0,697:0,698:0,699:0,700:0,701:0,702:0,703:0,704:0,705:0,706:0,707:0,708:0,709:0,710:0,711:0,712:0,713:0,714:0,715:0,716:0,717:0,718:0,719:0,720:0,721:0,722:0,723:0,724:0,725:0,726:0,727:0,728:0,729:0,730:0,731:0,732:0,733:0,734:0,735:0,736:0,737:0,738:0,739:0,740:0,741:0,742:0,743:0,744:0,745:0,746:0,747:0,748:0,749:0,750:0,751:0,752:0,753:0,754:0,755:0,756:0,757:0,758:0,759:0,760:0,761:0,762:0,763:0,764:0,765:0,766:0,767:0,768:0,769:0,770:0,771:0,772:0,773:0,774:0,775:0,776:0,777:0,778:0,779:0,780:0,781:0,782:0,783:0,784:0,785:0,786:0,787:0,788:0,789:0,790:0,791:0,792:0,793:0,794:0,795:0,796:0,797:0,798:0,799:0,800:0,801:0,802:0,803:0,804:0,805:0,806:0,807:0,808:0,809:0,810:0,811:0,812:0,813:0,814:0,815:0,816:0,817:0,818:0,819:0,820:0,821:0,822:0,823:0,824:0,825:0,826:0,827:0,828:0,829:0,830:0,831:0,832:0,833:0,834:0,835:0,836:0,837:0,838:0,839:0,840:0,841:0,842:0,843:0,844:0,845:0,846:0,847:0,848:0,849:0,850:0,851:0,852:0,853:0,854:0,855:0,856:0,857:0,858:0,859:0,860:0,861:0,862:0,863:0,864:0,865:0,866:0,867:0,868:0,869:0,870:0,871:0,872:0,873:0,874:0,875:0,876:0,877:0,878:0,879:0,880:0,881:0,882:0,883:0,884:0,885:0,886:0,887:0,888:0,889:0,890:0,891:0,892:0,893:0,894:0,895:0,896:0,897:0,898:0,899:0,900:0,901:0,902:0,903:0,904:0,905:0,906:0,907:0,908:0,909:0,910:0,911:0,912:0,913:0,914:0,915:0,916:0,917:0,918:0,919:0,920:0,921:0,922:0,923:0,924:0,925:0,926:0,927:0,928:0,929:0,930:0,931:0,932:0,933:0,934:0,935:0,936:0,937:0,938:0,939:0,940:0,941:0,942:0,943:0,944:0,945:0,946:0,947:0,948:0,949:0,950:0,951:0,952:0,953:0,954:0,955:0,956:0,957:0,958:0,959:0,960:0,961:0,962:0,963:0,964:0,965:0,966:0,967:0,968:0,969:0,970:0,971:0,972:0,973:0,974:0,975:0,976:0,977:0,978:0,979:0,980:0,981:0,982:0,983:0,984:0,985:0,986:0,987:0,988:0,989:0,990:0,991:0,992:0,993:0,994:0,995:0,996:0,997:0,998:0,999:0,1000:0}
for i in IM1:
    IM[pc]=i
    pc+=4

def binToInt(strr):
    if(strr[0]=='1'):
        #-ve no
        strr="".join('1' if k=='0' else '0' for k in strr)
        temp=1+int(strr,2)
        return -temp
    else:
        return int(strr,2)

def IntToBin(num):
    if(num>=0):
        return bin(num)[2:].zfill(32)
    
    else:
        str=bin(num)[3:].zfill(32)
        temp=""
        #print(temp)
        for i in range(len(str)-1,-1,-1):
            if(str[i]=='1'):
                k=i
                break
        for one in range(k):
            if(str[one]=='0'):
                temp+='1'
            elif(str[one]=="1"):
                temp+='0'
        
        temp=temp+str[k:]
        return temp



def sign_extend(val):
    if(val[0]=='0'):
        val=val.zfill(32)
        return val
    else:
        val='1111111111111111'+val
        return val

def srl(reg, shamt):
    if(shamt >= len(IntToBin(reg))):
        a = '0'*32
        return binToInt(a)
    else:
        a = ('0'*shamt +  IntToBin(reg)[0:-shamt])
        return binToInt(a)


class Processor:
    def __init__(self):
        self.instr='i'#this is a control sig which helps in the execute phase for different format instructions(i,r,j)
        self.PC = 0
        self.reg_val = {'$0': 0,'$at': 0,'$v0': 0,'$v1': 0,'$a0': 0,'$a1': 0,'$a2': 0,'$a3': 0,'$t0': 0,'$t1': 0,'$t2': 0,'$t3': 0,'$t4': 0,'$t5': 0,'$t6': 0,'$t7': 0,'$s0': 0,'$s1': 0,'$s2': 0,'$s3': 0,'$s4': 0,'$s5': 0,'$s6': 0,'$s7': 0,'$t8': 0,'$t9': 0}
        self.reg = ['$0','$at','$v0','$v1','$a0','$a1','$a2','$a3','$t0','$t1','$t2','$t3','$t4','$t5','$t6','$t7','$s0','$s1','$s2','$s3','$s4','$s5','$s6','$s7','$t8','$t9']
        #these are some of the input prompts that we use in the simulation
        self.count=0
        self.opCount=0
        self.prompt1="Enter the size of the array: "
        self.prompt2="Enter the input: "
        self.prompt3="Enter the value of k: "
        self.prompt4="Enter the value of sum: "
        self.op="Output:"
        #---------------
        self.exit=False#this is a control signal which becomes True when the final exit syscall is encountered


    def Fetch(self, IM):#this is the IF stage
        inst = IM[self.PC]
        # self.PC += 1
        self.PC += 4
        return inst
    
    def Decode(self, inst: str):#this is the DECODE/REGISTER READ stage
        #the decode stage returns a tuple which contains the fields that are needed by different instructions in their execute phase
        op = inst[0:6]
        rs = inst[6:11]
        rt = inst[11:16]
        rd = inst[16:21]
        shamt = inst[21:26]
        func = inst[26:32]

        if(op == '000000'):#rformats have 0 as opcode
            self.instr='r'#this is a control signal for the execute stage
            rs = self.reconReg(rs)
            rt = self.reconReg(rt)
            rd = self.reconReg(rd)
            func = self.DecodeFunc(func)
            return(rs, rt, rd,int(shamt,2), func)#this is the tuple containing all the fields that will be used by a R-format instruction in the later stages
        
        elif(op=='000010'):#jump
            self.instr='j'
            addr='0000'+inst[6:]+'00'#only 26 bit address given in the instruction for jump, so we append 0s in the beginning and ending
            return (op,int(addr,2))
        
        elif(op=='011100'):#mul--> this acts like r-format but its opcode isn't 0
            self.instr='mul'
            rs = self.reconReg(rs)
            rt = self.reconReg(rt)
            rd = self.reconReg(rd)
            return(rs, rt, rd)

        else:#i format
            self.instr='i'
            imm=inst[16:]
            imm=sign_extend(imm)#sign extending the immediate value
            rs = self.reconReg(rs)
            rt = self.reconReg(rt)
            funcc=self.DecodeI(op)
            return (funcc,rs,rt,binToInt(imm))


    def Execute(self, dec: tuple):#this is the stage where ALU operations, syscall(printing, input taking, etc. ) are performed
        #if the instruction doesn't do writeback then we return tuple (None,None)
        ### R-FORMAT ###
        if(self.instr=='r'):#sll#d0-->rs,d1-->rt,d2-->rd, d4-->funcc
            # print(dec[4],'r')
            if(dec[4] == 'add'):
                res = self.reg_val[dec[0]] + self.reg_val[dec[1]]
                return (res, dec[2])#the returning tuples are for the WB stage
            elif(dec[4] == 'sub'):
                res = self.reg_val[dec[0]] - self.reg_val[dec[1]]
                return (res, dec[2])
            elif(dec[4] == 'mul'):##
                res = self.reg_val[dec[0]] * self.reg_val[dec[1]]
                return (res, dec[2])
            elif(dec[4] == 'div'):###
                res = self.reg_val[dec[0]] // self.reg_val[dec[1]]
                return (res, dec[2])
            elif(dec[4] == 'and'):
                res = self.reg_val[dec[0]] & self.reg_val[dec[1]]
                return (res, dec[2])
            elif(dec[4] == 'or'):
                res = self.reg_val[dec[0]] | self.reg_val[dec[1]]
                return (res, dec[2])
            elif(dec[4] == 'addu'):
                res = self.reg_val[dec[0]] + self.reg_val[dec[1]]
                return (res, dec[2])
            
            elif(dec[4] == 'subu'):
                res = self.reg_val[dec[0]] - self.reg_val[dec[1]]
                return (res, dec[2])
            
            elif(dec[4] == 'sll'):#sll#d0-->rs,d1-->rt,d2-->rd, d4-->funcc
                #rd=rt<<shamt   #directly used py left shift for it!
                res = self.reg_val[dec[1]]<<dec[3]
                return (res, dec[2])

            elif(dec[4] == 'srl'):#made a special function for it
                res=srl(self.reg_val[dec[1]], dec[3])
                return (res, dec[2])

            elif(dec[4] == 'sra'):#normal python right shift is sra
                res = self.reg_val[dec[1]]>>dec[3]
                return (res, dec[2])
            
            elif(dec[4] == 'slt'):#d0-->rs,d1-->rt,d2-->rd
                if(self.reg_val[dec[0]]<self.reg_val[dec[1]]):
                    res=1
                else:
                    res=0
                return (res, dec[2])
            
            elif(dec[4] == 'syscall'):#syscall!!##as we don't know exact working of syscall so we directly write to $v0
                if(self.reg_val['$v0']==5):#take input here
                    inputPrompt=""
                    if(self.count==0):#the initial prompt will be for taking the size of array
                        inputPrompt=self.prompt1
                        self.count+=1
                    else:#the other prompts will be for entering array elements
                        inputPrompt=self.prompt2

                    self.reg_val['$v0']=int(input(inputPrompt))
                    return (None,None)
                
                elif(self.reg_val['$v0']==10):#exit condition
                    self.exit=True
                    
                elif(self.reg_val['$v0'] == 1):#printing integer
                    if(self.opCount==0):
                        print(self.op,self.reg_val['$a0'],end=" ")
                        self.opCount+=1
                    else:
                        print(self.reg_val['$a0'],end=" ")

                    return (None,None)
                
                elif(self.reg_val['$v0'] == 4):#printing space
                    print("", end="")
                    return (None,None)
            
        #the mul instruction looks like r-format but it's opcode isn't 0, so we decode it separately
                
        elif(self.instr=='mul'):#this is a special instrn of mars
            # print('mul')
            res=self.reg_val[dec[0]]*self.reg_val[dec[1]]#rs*rt
            return (res,dec[2])
                    
            ### I-FORMAT ###
        #d[1]-->rs,d[2]-->rt,d[3]-->imm
        elif(self.instr=='i'):##dec[3] is imm value
            # print(dec[0],'i')
            if(dec[0] == 'beq'):
                if(self.reg_val[dec[1]] == self.reg_val[dec[2]]):
                    self.PC += 4*dec[3]
                return (None,None)
            elif(dec[0] == 'bne'):
                if(self.reg_val[dec[1]] != self.reg_val[dec[2]]):
                    self.PC += 4*dec[3]
                return (None,None)
                
            elif(dec[0] == 'addi' or dec[0]=='addiu'):
                res = self.reg_val[dec[1]] + dec[3]
                return(res, dec[2])
            elif(dec[0] == 'subi'or dec[0]=='subiu'):
                res = self.reg_val[dec[1]] - dec[3]
                return(res, dec[2])
            elif(dec[0] == 'muli'):
                res = self.reg_val[dec[1]] * dec[3]
                return(res, dec[2])
            elif(dec[0] == 'divi'):
                res = self.reg_val[dec[1]] // dec[3]
                return(res, dec[2])
            elif(dec[0] == 'andi'):
                res = self.reg_val[dec[1]] & dec[3]
                return(res, dec[2])
            elif(dec[0] == 'ori'):
                res = self.reg_val[dec[1]] | dec[3]
                return(res, dec[2])
            elif(dec[0] == 'lui'):#loading the upper 16 bits of rt and making lower 16 bits to 0
                dec[3]<<=16
                res = dec[3]
                return(res, dec[2])
            
                #will call memory method for lw and sw only
            
            elif(dec[0] == 'sw'):##sw
                addr=self.reg_val[dec[1]]+dec[3]
                return self.Memory(addr,dec[2],'write')
            
            elif(dec[0] == 'lw'):##lw  
                addr=self.reg_val[dec[1]]+dec[3]
                return self.Memory(addr, dec[2],'read')

            ### JMP-FORMAT ###

        else:#j format
            #print("jump")
            self.PC = dec[1]
            return (None, None)
        
    def Memory(self,addr,reg,control_signal):#MEM stage is used only be lw and sw
        if(control_signal=='read'):
            res=DM[addr]
            return (res,reg)
        elif(control_signal=='write'):
            DM[addr]=self.reg_val[reg]
            return (None,None)#this None tuple indicates that nothing will happen in write back stage

    def WriteBack(self, dec: tuple):
        #first we check if the instruction does WB or not
        #if the first element of the tuple returned by ex stage is None, that means no WB
        if(dec[0] != None):#There exist a register to writeback incase the instruction was not jump
            self.reg_val[dec[1]] = dec[0]
    
    #-------------------------------------5 stages are over-------------------------#
    #now no of the auxiliary functions for the simulation are written 
    def reconReg(self, val):
        return self.reg[int(val, 2)]
    
    def DecodeI(self,val):
        #to decode I- format instructions
        if( val=='000100'):
            return 'beq'
        elif( val=='000101'):
            return 'bne'
        elif( val=='001000'):
            return 'addi'
        elif( val=='001111'):
            return 'lui'
        elif( val=='101011'):
            return 'sw'
        elif( val=='100011'):
            return 'lw'
        elif( val=='001001'):
            return 'addiu'
        elif( val=='001101'):
            return 'ori'


    def DecodeFunc(self,val):#used for r formats
        #to decode the funcn field of r format instrns
        if(val=='100000' ):#for add and addu
            return 'add'
        elif( val=='100001'):
            return 'addu'
        elif( val=='100100'):
            return 'and'
        elif( val=='100010'):
            return 'sub'
        elif( val=='100101'):
            return 'or'
        elif( val=='000000'):
            return 'sll'
        elif( val=='000011'):
            return 'sra'
        elif( val=='000010'):
            return 'srl'
        elif( val=='001100'):
            return 'syscall'
        elif( val=='101010'):
            return 'slt'
        elif( val=='011000'):
            return 'mul'
        elif( val=='011010'):
            return 'div'


mips = Processor()
while True:
    inst = mips.Fetch(IM)
    info = mips.Decode(inst)
    val = mips.Execute(info)
    if(mips.exit):#if exit syscall is encountered then mips.exit==True
        break
    mips.WriteBack(val)


#after simulating all the instructions, we print the values of all the registers in a table
    
df = pd.DataFrame(list(mips.reg_val.items()), columns=['register', 'value'])
table = tabulate.tabulate(df, headers='keys', tablefmt='rounded_grid', showindex=False)
print()
print(table)