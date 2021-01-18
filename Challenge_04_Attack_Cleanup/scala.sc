string rtn;
int acc = 0;
for (auto& c : message) {
  if (c >= '0' && c <= '9') acc = acc * 10 + c - '0';
  else {
    if (c == 'z') rtn.append(acc==0?1:acc, 'a');
    else if (c == 'g') rtn.append(acc==0?1:acc, 't');
    else if (c == 't') rtn.append(acc==0?1:acc, 'g');
    else if (c == 'x') rtn.append(acc==0?1:acc, 'c');
    acc = 0;
  }
}
return rtn;
