# O(LOG(MIN(M,N)))

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m  # نطاق البحث في المصفوفة الأصغر

        while low <= high:
            # حساب مؤشرات التقسيم في كلا المصفوفتين
            partition_x = (low + high) // 2
            partition_y = (m + n + 1) // 2 - partition_x

            # حالات خاصة: التعامل مع الأقسام الفارغة
            max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
            min_right_x = float('inf') if partition_x == m else nums1[partition_x]

            max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
            min_right_y = float('inf') if partition_y == n else nums2[partition_y]


            # التحقق مما إذا وجدنا الأقسام الصحيحة
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                # حساب الوسيط بناءً على ما إذا كان الطول الإجمالي فرديًا أو زوجيًا
                if (m + n) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                else:
                    return max(max_left_x, max_left_y)
            elif max_left_x > min_right_y:

                # القسم في nums1 بعيد جدًا إلى اليمين، نتحرك إلى اليسار
                high = partition_x - 1
            else:
                # القسم في nums1 بعيد جدًا إلى اليسار، نتحرك إلى اليمين
                low = partition_x + 1