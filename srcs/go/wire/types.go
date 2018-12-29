package wire

// #include <kungfu.h>
import "C"

type KungFu_Datatype C.KungFu_Datatype

var (
// uncommented if required
// KungFu_INT32  = KungFu_Datatype(C.KungFu_INT32)
// KungFu_FLOAT  = KungFu_Datatype(C.KungFu_FLOAT)
// KungFu_DOUBLE = KungFu_Datatype(C.KungFu_DOUBLE)
)

func (dtype KungFu_Datatype) Size() int {
	return int(C.kungfu_type_size(C.KungFu_Datatype(dtype)))
}

type KungFu_Op C.KungFu_Op

var (
// uncommented if required
// KungFu_SUM KungFu_Op = KungFu_Op(C.KungFu_SUM)
// KungFu_MIN KungFu_Op = KungFu_Op(C.KungFu_MIN)
// KungFu_MAX KungFu_Op = KungFu_Op(C.KungFu_MAX)
)

type KungFu_AllReduceAlgo C.KungFu_AllReduceAlgo

var (
	KungFu_Simple = KungFu_AllReduceAlgo(C.KungFu_SimpleAllReduce)
	KungFu_Ring   = KungFu_AllReduceAlgo(C.KungFu_RingAllReduce)
	KungFu_Clique = KungFu_AllReduceAlgo(C.KungFu_FullSymmetricAllReduce)
	KungFu_Tree   = KungFu_AllReduceAlgo(C.KungFu_TreeAllReduce)

	algoNames = map[KungFu_AllReduceAlgo]string{
		KungFu_Simple: `SIMPLE`,
		KungFu_Ring:   `RING`,
		KungFu_Clique: `CLIQUE`,
		KungFu_Tree:   `TREE`,
	}
)

func (a KungFu_AllReduceAlgo) String() string {
	for k, v := range algoNames {
		if a == k {
			return v
		}
	}
	return `TREE`
}

func ParseAlgo(s string) KungFu_AllReduceAlgo {
	for k, v := range algoNames {
		if s == v {
			return k
		}
	}
	return KungFu_Tree
}