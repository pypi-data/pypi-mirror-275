/* Philip T.L.C. Clausen Jan 2017 plan@dtu.dk */

/*
 * Copyright (c) 2017, Philip Clausen, Technical University of Denmark
 * All rights reserved.
 * 
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 *		http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
*/

#ifndef QSEQS
typedef struct qseqs Qseqs;
struct qseqs {
	unsigned size;
	unsigned len;
	unsigned char *seq;
};
#define QSEQS 1
#endif

/* initialize Qseqs */
Qseqs * setQseqs(unsigned size);
/* destroy Qseqs */
void destroyQseqs(Qseqs *dest);
void insertKmerBound(Qseqs *header, int start, int end);
void qseq2nibble(Qseqs *src, long unsigned *dest);
