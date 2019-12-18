#pragma once

#ifdef __cplusplus
extern "C" {
#endif

enum KungFu_Strategy {
    KungFu_Tree,
    KungFu_BinaryTree,
    KungFu_Ring,
    KungFu_Star,
    KungFu_Clique,
    KungFu_BinaryTreeStar,
    KungFu_AUTO,
    KungFu_BinaryTreePrimaryBackup
};

typedef enum KungFu_Strategy KungFu_Strategy;

#ifdef __cplusplus
}
#endif
