def mushrooms(A, k, m):
 n = len(A)
 result = 0
 pref = prefix_sums(A)
 for p in xrange(min(m, k) + 1):
 left_pos = k - p
 right_pos = min(n - 1, max(k, k + m - 2 * p))
 result = max(result, count_total(pref, left_pos, right_pos))
 for p in xrange(min(m + 1, n - k)):
 right_pos = k + p
 left_pos = max(0, min(k, k - (m - 2 * p)))
 result = max(result, count_total(pref, left_pos, right_pos))
 return result
